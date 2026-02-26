"""Generate a full gallery for a2i2 and all conference presets."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401
from scienceplots import PRESET_SPECS


OUTDIR = Path(__file__).resolve().parent / "figures"
OUTDIR.mkdir(parents=True, exist_ok=True)


def _save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(OUTDIR / filename, dpi=300)
    plt.close(fig)


def _line(ax: plt.Axes) -> None:
    x = np.linspace(0, 8, 250)
    ax.plot(x, np.sin(x), label="A")
    ax.plot(x, np.cos(x / 2), label="B")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(frameon=False)


def _bar(ax: plt.Axes) -> None:
    cats = ["B", "S", "M", "L"]
    vals = [68, 73, 77, 80]
    ax.bar(cats, vals)
    ax.set_ylabel("Score")


def _scatter(ax: plt.Axes) -> None:
    rng = np.random.default_rng(7)
    x = rng.normal(0.0, 1.0, 150)
    y = x + rng.normal(0.0, 0.45, 150)
    ax.scatter(x, y, alpha=0.8)
    ax.set_xlabel("Dim 1")
    ax.set_ylabel("Dim 2")


def _heatmap(ax: plt.Axes, fig: plt.Figure) -> None:
    rng = np.random.default_rng(11)
    data = rng.random((10, 10))
    img = ax.imshow(data, cmap="viridis")
    fig.colorbar(img, ax=ax, fraction=0.046, pad=0.04)


def _image_grid(fig: plt.Figure) -> None:
    rng = np.random.default_rng(13)
    axes = fig.subplots(2, 3)
    for idx, ax in enumerate(axes.ravel(), start=1):
        ax.imshow(rng.random((28, 28)), cmap="magma")
        ax.set_title(f"Img {idx}")
        ax.set_xticks([])
        ax.set_yticks([])


def _text_equation(ax: plt.Axes, preset_name: str) -> None:
    ax.axis("off")
    ax.text(0.02, 0.8, "Token-level objective", fontsize=10)
    ax.text(0.02, 0.52, r"$L = \sum_t -\log p(y_t|x, y_{<t})$", fontsize=10)
    ax.text(0.02, 0.28, f"Preset: {preset_name}", fontsize=8)


def _render_preset(preset_name: str) -> None:
    figure_type = str(PRESET_SPECS[preset_name]["figure_type"])
    styles = ["science", preset_name, "no-latex"]
    with plt.style.context(styles):
        if figure_type == "image-grid":
            fig = plt.figure()
            _image_grid(fig)
        else:
            fig, ax = plt.subplots()
            if figure_type == "line":
                _line(ax)
            elif figure_type == "bar":
                _bar(ax)
            elif figure_type == "scatter":
                _scatter(ax)
            elif figure_type == "heatmap":
                _heatmap(ax, fig)
            else:
                _text_equation(ax, preset_name)
        _save(fig, f"style-preview-{preset_name}.png")


def _render_a2i2() -> None:
    x = np.linspace(-2.5, 2.5, 400)
    with plt.style.context(["a2i2", "no-latex"]):
        fig, ax = plt.subplots(figsize=(3.4, 2.5))
        ax.plot(x, 1 / (1 + np.exp(-x)), label="sigmoid")
        ax.plot(x, 0.5 * (np.tanh(1.5 * x) + 1), label="scaled tanh")
        ax.set_xlabel("x")
        ax.set_ylabel("response")
        ax.legend(frameon=False)
        _save(fig, "style-preview-a2i2.png")


if __name__ == "__main__":
    _render_a2i2()
    for preset in sorted(PRESET_SPECS):
        _render_preset(preset)
