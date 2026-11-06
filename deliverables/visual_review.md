# Visual review of completed inference

Reviewed on 2026-11-06 by the agent. Evidence sheets are in `figures/review/`; each successful run has a `visual_review.json` record. These are sampled qualitative reviews, not exhaustive temporal or all-episode certification.

## Minecraft

For each of eight conditions, all eight generated videos were inspected at frame 0, frame 2, quarter, middle, three-quarter and the last two frames (deduplicated for short clips). Recognizable terrain, trees and sky persist and scenes change across sampled frames. No obvious blank-frame padding, uniform intensity saturation or complete freezing was seen in these frames. Local geometry stretches, soft textures, foliage changes and appearing/disappearing objects remain visible, especially on long rollouts. These observations support the limited absence-of-gross-collapse conclusion, not physical consistency or prediction accuracy. Numeric finite checks and temporal metrics cover all saved frames; original unclamped values can exceed [0,1], and display/metrics clamp them.

## Maze2D

Inspected all 16 final predicted-plan images and all 16 interaction images saved by each of 14 runs, totaling 448 images. Paths and goal markers render in the maze view. Stronger guidance generally produces more direct successful interaction routes, while low guidance shows loops and incomplete trajectories. Failures and detours remain in large mazes at higher scales. Predicted plans can approach/cross wall cells, and the plan and executed trajectory need not coincide. The figures do not certify collision-free planning. The other 112 episodes per run have quantitative metrics but no saved images in this run; visual coverage must not be described as all 1,792 episodes.

## Interpretation

Temporal change is not future prediction accuracy. Descriptive SDs across videos or episodes are not confidence intervals; only default maze guidance has repeated model seeds, with fixed environment seed zero. No consistent quality ranking of video schedules is established. The paper's planning baselines and normalized scores are not matched by this released protocol.
