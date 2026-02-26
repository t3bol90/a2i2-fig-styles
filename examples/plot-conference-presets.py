"""Generate representative PNG outputs for conference figure presets."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from scienceplots import get_preset, style_stack


OUTDIR = Path(__file__).resolve().parent / "figures"
OUTDIR.mkdir(parents=True, exist_ok=True)


def _save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(OUTDIR / filename, dpi=300)
    plt.close(fig)


def make_line_plot() -> None:
    x = np.linspace(0, 10, 300)
    y1 = np.sin(x)
    y2 = np.cos(x / 2)
    styles = style_stack("neurips", "1col", "line", no_latex=True)
    with plt.style.context(styles):
        fig, ax = plt.subplots()
        ax.plot(x, y1, label="sin(x)")
        ax.plot(x, y2, label="cos(x/2)")
        ax.set_xlabel("Epoch")
        ax.set_ylabel("Score")
        ax.legend()
        _save(fig, "preset-neurips-1col-line.png")


def make_bar_plot() -> None:
    models = ["Base", "Small", "Medium", "Large"]
    vals = [71.1, 74.8, 77.3, 79.2]
    styles = style_stack("acl", "2col", "bar", no_latex=True)
    with plt.style.context(styles):
        fig, ax = plt.subplots()
        ax.bar(models, vals)
        ax.set_ylabel("BLEU")
        ax.set_title("ACL 2-column bar")
        _save(fig, "preset-acl-2col-bar.png")


def make_scatter_plot() -> None:
    rng = np.random.default_rng(8)
    x = rng.normal(0.0, 1.0, 140)
    y = x + rng.normal(0.0, 0.4, 140)
    styles = style_stack("kdd", "1col", "scatter", no_latex=True)
    with plt.style.context(styles):
        fig, ax = plt.subplots()
        ax.scatter(x, y, alpha=0.8)
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        ax.set_title("KDD 1-column scatter")
        _save(fig, "preset-kdd-1col-scatter.png")


def make_heatmap_plot() -> None:
    rng = np.random.default_rng(0)
    data = rng.random((12, 12))
    styles = style_stack("icdm", "2col", "heatmap", no_latex=True)
    with plt.style.context(styles):
        fig, ax = plt.subplots()
        image = ax.imshow(data, cmap="viridis")
        fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
        ax.set_title("ICDM 2-column heatmap")
        _save(fig, "preset-icdm-2col-heatmap.png")


def make_image_grid_plot() -> None:
    rng = np.random.default_rng(2)
    styles = style_stack("neurips", "2col", "image-grid", no_latex=True)
    with plt.style.context(styles):
        fig, axes = plt.subplots(2, 3)
        for idx, ax in enumerate(axes.ravel(), start=1):
            data = rng.random((32, 32))
            ax.imshow(data, cmap="magma")
            ax.set_title(f"Img {idx}")
            ax.set_xticks([])
            ax.set_yticks([])
        _save(fig, "preset-neurips-2col-image-grid.png")


def make_text_equation_plot() -> None:
    styles = style_stack("acl", "1col", "text-equation", no_latex=True)
    with plt.style.context(styles):
        fig, ax = plt.subplots()
        ax.axis("off")
        preset = get_preset("acl", "1col", "text-equation")
        ax.text(0.02, 0.8, "LLM objective", fontsize=10)
        ax.text(0.02, 0.55, r"$L = \sum_t -\log p(y_t|x, y_{<t})$", fontsize=10)
        ax.text(0.02, 0.3, f"Preset: {preset['name']}", fontsize=9)
        _save(fig, "preset-acl-1col-text-equation.png")


if __name__ == "__main__":
    make_line_plot()
    make_bar_plot()
    make_scatter_plot()
    make_heatmap_plot()
    make_image_grid_plot()
    make_text_equation_plot()
