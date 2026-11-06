import os
from omegaconf import DictConfig
import torch
from lightning.pytorch.utilities.types import STEP_OUTPUT
from algorithms.common.metrics import (
    FrechetInceptionDistance,
    LearnedPerceptualImagePatchSimilarity,
    FrechetVideoDistance,
)
from .df_base import DiffusionForcingBase
from utils.logging_utils import log_video, get_validation_metrics_for_videos


class DiffusionForcingVideo(DiffusionForcingBase):
    """
    A video prediction algorithm using Diffusion Forcing.
    """

    def __init__(self, cfg: DictConfig):
        self.metrics = cfg.metrics
        self.n_tokens = cfg.n_frames // cfg.frame_stack  # number of max tokens for the model
        super().__init__(cfg)

    def _build_model(self):
        super()._build_model()
        self.validation_fid_model = FrechetInceptionDistance(feature=64) if "fid" in self.metrics else None
        self.validation_lpips_model = LearnedPerceptualImagePatchSimilarity() if "lpips" in self.metrics else None
        self.validation_fvd_model = [FrechetVideoDistance()] if "fvd" in self.metrics else None

    def training_step(self, batch, batch_idx) -> STEP_OUTPUT:
        output_dict = super().training_step(batch, batch_idx)
        # log the video
        if batch_idx % 5000 == 0 and self.logger:
            log_video(
                output_dict["xs_pred"],
                output_dict["xs"],
                step=self.global_step,
                namespace="training_vis",
                logger=self.logger.experiment,
            )
        return output_dict

    def validation_step(self, batch, batch_idx):
        # Preserve the dataset's validity mask; do not infer padding from black pixels.
        if os.environ.get("DF_DUMP_DIR"):
            if not hasattr(self, "_dump_valid"):
                self._dump_valid = []
            self._dump_valid.append(torch.as_tensor(batch[-1]).T.bool().cpu())
        return super().validation_step(batch, batch_idx)

    def on_validation_epoch_end(self, namespace="validation") -> None:
        if not self.validation_step_outputs:
            return
        xs_pred = []
        xs = []
        for pred, gt in self.validation_step_outputs:
            xs_pred.append(pred)
            xs.append(gt)
        xs_pred = torch.cat(xs_pred, 1)
        xs = torch.cat(xs, 1)

        dump_dir = os.environ.get("DF_DUMP_DIR")
        if dump_dir:
            os.makedirs(dump_dir, exist_ok=True)
            torch.save({"pred": xs_pred.float().cpu(), "gt": xs.float().cpu(),
                        "context_frames": self.context_frames,
                        "valid": torch.cat(self._dump_valid, 1)},
                       os.path.join(dump_dir, f"{namespace}_samples.pt"))
            self._dump_valid.clear()

        if self.logger:
            log_video(
                xs_pred,
                xs,
                step=None if namespace == "test" else self.global_step,
                namespace=namespace + "_vis",
                context_frames=self.context_frames,
                logger=self.logger.experiment,
            )

        metric_dict = get_validation_metrics_for_videos(
            xs_pred[self.context_frames :],
            xs[self.context_frames :],
            lpips_model=self.validation_lpips_model,
            fid_model=self.validation_fid_model,
            fvd_model=(self.validation_fvd_model[0] if self.validation_fvd_model else None),
        )
        self.log_dict(
            {f"{namespace}/{k}": v for k, v in metric_dict.items()},
            on_step=False,
            on_epoch=True,
            prog_bar=True,
        )

        self.validation_step_outputs.clear()
