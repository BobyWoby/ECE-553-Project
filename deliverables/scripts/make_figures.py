#!/usr/bin/env python3
"""Render measured CSV/tensor outputs. Never synthesize missing experimental data."""
import argparse
import csv
import json
import re
import shutil
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

plt.rcParams.update({'font.size': 8, 'axes.labelsize': 8, 'axes.titlesize': 9,
                     'legend.fontsize': 8, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
                     'pdf.fonttype': 42})
MULTIPLIERS = [1, 2, 4, 8]
STYLES = ['-', '--', '-.', ':']
COLORS = ['#0072B2', '#D55E00', '#009E73', '#CC79A7']
SCHEMES = {'ar': 'Autoregressive stabilization', 'fs2': 'Full-sequence chunk 2'}


def read_csv(path):
    with path.open() as handle:
        return list(csv.DictReader(handle))


def write_csv(path, records):
    if records:
        with path.open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(records[0]))
            writer.writeheader()
            writer.writerows(records)


def save(fig, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path.with_suffix('.pdf'))
    fig.savefig(path.with_suffix('.png'), dpi=300)
    plt.close(fig)


def parse_name(name):
    match = re.fullmatch(r'mc_(ar|fs2)_(\d+)x(?:_b\d+)?_s(\d+)', name)
    if not match:
        raise ValueError(f'Unrecognized video run name: {name}')
    scheme, multiplier, seed = match.groups()
    return scheme, int(multiplier), int(seed)


def originals(root, figures):
    sources = {
        'original_minecraft_fig8_9': 'df_minecraft_long_1.png',
        'original_maze_fig14': 'df_medium_close_mpc.png',
        'original_maze_fig15_medium': 'df_medium_close.png',
        'original_maze_fig15_large': 'df_large_close.png',
    }
    for stem, filename in sources.items():
        source = root / 'df_src/figures/appendix_vis' / filename
        if not source.exists():
            continue
        shutil.copy2(source, figures / (stem + '.png'))
        im = Image.open(source)
        fig = plt.figure(figsize=(6.8, 6.8 * im.height / im.width))
        ax = fig.add_axes([0, 0, 1, 1]); ax.imshow(im); ax.axis('off')
        fig.savefig(figures / (stem + '.pdf'))
        plt.close(fig)


def aggregate(root, tables):
    records = read_csv(tables / 'divergence_summary.csv')
    groups, seen = {}, set()
    for record in records:
        scheme, multiplier, seed = parse_name(record['run'])
        identity = (scheme, multiplier, seed)
        if identity in seen:
            raise ValueError(f'Duplicate seed/run condition {identity}; select one run before aggregation.')
        seen.add(identity)
        metadata = root / 'runs' / record['run'] / 'run.json'
        record['wall_seconds_per_video'] = (
            float(json.loads(metadata.read_text())['wall_seconds']) / int(record['videos'])
            if metadata.exists() else float('nan'))
        groups.setdefault((scheme, multiplier), []).append(record)
    output = []
    for (scheme, multiplier), group in sorted(groups.items()):
        row = dict(schedule=scheme, multiplier=multiplier, seeds=len(group),
                   videos=sum(int(v['videos']) for v in group),
                   error_bar_unit='seed_mean_SD' if len(group) > 1 else 'video_SD')
        for metric in ['mse', 'lpips']:
            values = np.array([float(v[f'{metric}_last_mean']) for v in group])
            row[f'late_{metric}_mean'] = float(values.mean())
            row[f'late_{metric}_std'] = (
                float(values.std(ddof=1)) if len(values) > 1
                else float(group[0][f'{metric}_last_video_std']))
        seconds = sum(float(v['wall_seconds_per_video']) * int(v['videos']) for v in group)
        row['wall_seconds_per_video'] = seconds / row['videos']
        output.append(row)
    write_csv(tables / 'ablation_per_run.csv', records)
    write_csv(tables / 'ablation_summary.csv', output)
    with (tables / 'ablation_summary.tex').open('w') as handle:
        handle.write(r'\begin{tabular}{llrrr}' + '\n' + r'\toprule' + '\n')
        handle.write(r'Schedule & Horizon & Late MSE & Late LPIPS & Seconds/video\\' + '\n' + r'\midrule' + '\n')
        for row in output:
            cells = [row['schedule'], f"{row['multiplier']}x"]
            cells += [f"{row[f'late_{metric}_mean']:.4g} $\\pm$ {row[f'late_{metric}_std']:.3g}"
                      for metric in ['mse', 'lpips']]
            cells += [f"{row['wall_seconds_per_video']:.2f}"]
            handle.write(' & '.join(cells) + r'\\' + '\n')
        handle.write(r'\bottomrule' + '\n' + r'\end{tabular}' + '\n')
    return records, groups, output


def curve_figures(groups, tables, figures):
    active = [s for s in SCHEMES if any(key[0] == s for key in groups)]
    for filename, metrics, labels in [
        ('ablation_curves', ['lpips', 'mse'], ['Frame-to-frame LPIPS', 'Frame-to-frame MSE']),
        ('sanity_curves', ['intensity', 'pixel_std'], ['Mean pixel intensity [0,1]', 'Spatial pixel standard deviation']),
    ]:
        fig, axes = plt.subplots(2, len(active), figsize=(6.8 if len(active) == 2 else 3.3, 4.8),
                                 squeeze=False, sharex=True, layout='constrained')
        for column, scheme in enumerate(active):
            available = sorted(m for s, m in groups if s == scheme)
            ref_run = sorted(groups[(scheme, max(available))], key=lambda r: parse_name(r['run'])[2])[0]['run']
            gt = read_csv(tables / f'ground_truth_{ref_run}.csv')
            for row, (metric, label) in enumerate(zip(metrics, labels)):
                ax = axes[row, column]
                for multiplier in available:
                    group = groups[(scheme, multiplier)]
                    data = [read_csv(tables / f"divergence_{v['run']}.csv") for v in group]
                    ts = np.array([int(v['t']) for v in data[0]])
                    if any([int(v['t']) for v in d] != ts.tolist() for d in data):
                        raise ValueError('Repeated seeds have unequal horizons.')
                    values = np.array([[float(v[metric + '_mean']) for v in d] for d in data])
                    mean = values.mean(axis=0)
                    i = MULTIPLIERS.index(multiplier)
                    ax.plot(ts, mean, color=COLORS[i], ls=STYLES[i], label=f'{multiplier}x')
                gx = np.array([int(v['t']) for v in gt])
                gy = np.array([float(v[metric + '_mean']) for v in gt])
                ax.plot(gx, gy, color='#555555', lw=1, label=f'GT ({max(available)}x clips)')
                if metric in ['lpips', 'mse']:
                    sd = np.array([float(v[metric + '_std']) for v in gt])
                    ax.fill_between(gx, np.maximum(0, gy - sd), gy + sd, color='gray', alpha=.18)
                for boundary in range(10, max(int(v['t']) for v in data[0]) + 1, 10):
                    ax.axvline(boundary, color='gray', ls='--', lw=.5)
                ax.set_ylabel(label)
                ax.set_xlabel('Frame index (after frame skip)')
                if row == 0:
                    ax.set_title(SCHEMES[scheme])
                ax.set_ylim(bottom=0)
                if metric == 'intensity': ax.set_ylim(0, 1)
            axes[0, column].legend(loc='upper center', bbox_to_anchor=(.5, 1.5), ncol=3)
        save(fig, figures / filename)


def summary_figure(summary, groups, tables, figures):
    per_video = read_csv(tables / 'divergence_per_video.csv')
    # A single seed/condition supplies the reference, avoiding duplicated GT across repeats/schedules.
    ref_key = max(groups, key=lambda k: (k[1], k[0] == 'ar'))
    ref_run = sorted(groups[ref_key], key=lambda r: parse_name(r['run'])[2])[0]['run']
    reference = [r for r in per_video if r['run'] == ref_run]
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 3.0), layout='constrained')
    for ax, metric in zip(axes, ['lpips', 'mse']):
        for scheme, style, color in [('ar', 'o-', '#0072B2'), ('fs2', 's--', '#D55E00')]:
            selected = sorted([r for r in summary if r['schedule'] == scheme], key=lambda r: r['multiplier'])
            if selected:
                ax.errorbar([r['multiplier'] for r in selected], [r[f'late_{metric}_mean'] for r in selected],
                            yerr=[r[f'late_{metric}_std'] for r in selected], fmt=style, color=color,
                            capsize=3, label=scheme)
        values = np.array([float(r['gt_' + metric]) for r in reference])
        mean, sd = np.nanmean(values), np.nanstd(values, ddof=1)
        ax.axhspan(max(0, mean - sd), mean + sd, color='gray', alpha=.18,
                   label=f'GT {ref_key[1]}x: video mean ± SD')
        ax.set_xlabel('Horizon multiplier'); ax.set_xticks(MULTIPLIERS)
        ax.set_ylabel('Late-window ' + metric.upper()); ax.set_ylim(bottom=0)
        ax.legend(loc='upper center', bbox_to_anchor=(.5, 1.38), ncol=1)
    save(fig, figures / 'ablation_summary')


def indices_for_strip(length, context):
    if length <= 8: return np.arange(length)
    return np.unique(np.r_[np.arange(min(context, 2)), np.linspace(context, length - 1, 8 - min(context, 2), dtype=int)])


def draw_frame(ax, tensor, title=None, context=False):
    ax.imshow(tensor.permute(1, 2, 0).numpy())
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(context); spine.set_color('#D55E00'); spine.set_linewidth(1.5)
    if title: ax.set_title(title, fontsize=8)


def filmstrips(root, records, figures):
    import torch
    import imageio.v2 as imageio
    (figures / 'frames').mkdir(exist_ok=True)
    first_samples = {}
    for record in records:
        name = record['run']; path = root / 'runs' / name / 'validation_samples.pt'
        data = torch.load(path, map_location='cpu', weights_only=True)
        pred, gt = data['pred'].clamp(0, 1), data['gt'].clamp(0, 1)
        valid, context = data['valid'], int(data['context_frames'])
        indices = indices_for_strip(len(pred), context); batch = min(2, pred.shape[1])
        fig, axes = plt.subplots(batch * 2, len(indices), figsize=(6.8, batch * 1.6 + .4), squeeze=False)
        fig.subplots_adjust(left=.085, right=.995, bottom=.02, top=.85, wspace=.03, hspace=.08)
        for video in range(batch):
            for column, t in enumerate(indices):
                title = f't={t}' + ('\ncontext' if t < context else '')
                draw_frame(axes[2 * video, column], pred[t, video], title if video == 0 else None, t < context)
                ax = axes[2 * video + 1, column]
                if t < len(gt) and valid[t, video]: draw_frame(ax, gt[t, video], context=t < context)
                else: ax.axis('off'); ax.text(.5, .5, 'No GT', ha='center', fontsize=8)
            for row, label in [(2 * video, f'Pred {video + 1}'), (2 * video + 1, f'GT {video + 1}')]:
                axes[row, 0].set_ylabel(label, fontsize=8)
        save(fig, figures / 'frames' / name)
        imageio.mimsave(figures / 'frames' / f'{name}.mp4',
                       [(frame.permute(1, 2, 0).numpy() * 255).astype('uint8') for frame in pred[:, 0]], fps=8)
        scheme, multiplier, seed = parse_name(name)
        if scheme == 'ar' and seed == 0 and multiplier in [1, 8]:
            first_samples[multiplier] = (pred[:, 0], context, indices)
    original = figures / 'original_minecraft_fig8_9.png'
    if original.exists() and {1, 8} <= first_samples.keys():
        fig = plt.figure(figsize=(6.8, 6.6))
        outer = fig.add_gridspec(3, 1, height_ratios=[3.5, 1, 1], left=.02, right=.99, top=.96, bottom=.03, hspace=.45)
        ax = fig.add_subplot(outer[0]); ax.imshow(Image.open(original)); ax.axis('off')
        ax.set_title('Original: Chen et al., Figures 8–9', fontsize=9)
        for row, multiplier in enumerate([1, 8], 1):
            pred, context, indices = first_samples[multiplier]
            anchor = fig.add_subplot(outer[row]); anchor.axis('off')
            anchor.text(0, 1.4, f'Ours: attention checkpoint, {multiplier}x horizon, video 1', transform=anchor.transAxes, fontsize=9)
            inner = outer[row].subgridspec(1, len(indices), wspace=.03)
            for column, t in enumerate(indices):
                draw_frame(fig.add_subplot(inner[column]), pred[t], f't={t}', t < context)
        save(fig, figures / 'r1_minecraft_compare')


def maze_comparisons(root, figures):
    (figures / 'maze').mkdir(exist_ok=True)
    for env, scale in [('medium', 3), ('large', 2)]:
        runs = sorted((root / 'runs').glob(f'maze_{env}_g{scale}_s0'))
        if not runs: continue
        for source in runs[0].glob('validation*_sample_*.png'):
            shutil.copy2(source, figures / 'maze' / (runs[0].name + '_' + source.name))
        original = figures / f'original_maze_fig15_{env}.png'
        plans = sorted(runs[0].glob('validation*_plan_sample_0.png'))
        if not (original.exists() and plans): continue
        own = plans[-1]
        fig = plt.figure(figsize=(6.8, 4.0), layout='constrained')
        grid = fig.add_gridspec(2, 2, height_ratios=[1, 2])
        axes = [fig.add_subplot(grid[0, :]), fig.add_subplot(grid[1, 0]), fig.add_subplot(grid[1, 1])]
        interaction = runs[0] / 'validation_interaction_sample_0.png'
        for ax, path, title in zip(axes, [original, own, interaction],
                                  ['Original: Figure 15', f'Ours: {env}, guidance {scale}, plan 0', 'Ours: executed trajectory 0']):
            ax.imshow(Image.open(path)); ax.axis('off'); ax.set_title(title)
        save(fig, figures / f'r2_{env}_compare')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path.home() / 'eecs553')
    parser.add_argument('--originals-only', action='store_true')
    args = parser.parse_args(); tables = args.root / 'deliverables/tables'; figures = args.root / 'deliverables/figures'
    figures.mkdir(parents=True, exist_ok=True)
    originals(args.root, figures)
    if args.originals_only: return
    maze_comparisons(args.root, figures)
    if not (tables / 'divergence_summary.csv').exists():
        raise SystemExit('No measured video summary; no empirical video figures generated.')
    records, groups, summary = aggregate(args.root, tables)
    curve_figures(groups, tables, figures)
    summary_figure(summary, groups, tables, figures)
    filmstrips(args.root, records, figures)


if __name__ == '__main__': main()
