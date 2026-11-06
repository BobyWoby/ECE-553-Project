#!/usr/bin/env python3
"""Regenerate the sampled visual-review evidence; does not approve any run."""
from pathlib import Path
import argparse
import torch
from PIL import Image, ImageDraw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    out = args.root / 'deliverables/figures/review'
    out.mkdir(parents=True, exist_ok=True)
    for path in sorted((args.root / 'runs').glob('mc_*/validation_samples.pt')):
        data = torch.load(path, map_location='cpu', weights_only=True)
        frames = data['pred'].clamp(0, 1)
        indices = sorted(set([0, int(data['context_frames']), len(frames)//4,
                              len(frames)//2, 3*len(frames)//4, len(frames)-2, len(frames)-1]))
        sheet = Image.new('RGB', (len(indices)*128, frames.shape[1]*148+30), 'white')
        draw = ImageDraw.Draw(sheet)
        draw.text((5, 5), path.parent.name, fill='black')
        for video in range(frames.shape[1]):
            for column, t in enumerate(indices):
                pixels = (frames[t, video].permute(1, 2, 0).numpy()*255).astype('uint8')
                sheet.paste(Image.fromarray(pixels), (column*128, 30+video*148))
                draw.text((column*128, 158+video*148), f'v{video} t{t}', fill='black')
        sheet.save(out / (path.parent.name+'.png'))
    for folder in sorted((args.root / 'runs').glob('maze_*')):
        files = sorted(folder.glob('validation*_sample_*.png'))
        if not files:
            continue
        sheet = Image.new('RGB', (8*180, ((len(files)+7)//8)*200+30), 'white')
        draw = ImageDraw.Draw(sheet)
        draw.text((5, 5), folder.name, fill='black')
        for i, path in enumerate(files):
            picture = Image.open(path).convert('RGB')
            picture.thumbnail((180, 175))
            x, y = (i % 8)*180, 30+(i//8)*200
            sheet.paste(picture, (x, y))
            draw.text((x, y+175), path.name.replace('validation', ''), fill='black')
        sheet.save(out / (folder.name+'.png'))


if __name__ == '__main__':
    main()
