"""Generate example PNG figures using the A2I2 Matplotlib style."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scienceplots  # noqa: F401


OUTDIR = Path(__file__).resolve().parent / "figures"
OUTDIR.mkdir(parents=True, exist_ok=True)


def save_response_curve() -> None:
    x = np.linspace(-3, 3, 400)
    y_sigmoid = 1 / (1 + np.exp(-x))
    y_tanh = 0.5 * (np.tanh(1.5 * x) + 1)
    y_softplus = np.log1p(np.exp(x)) / np.log(1 + np.exp(3))

    with plt.style.context(["a2i2", "no-latex"]):
        fig, ax = plt.subplots(figsize=(3.4, 2.5))
        ax.plot(x, y_sigmoid, label="sigmoid")
        ax.plot(x, y_tanh, label="scaled tanh")
        ax.plot(x, y_softplus, label="normalized softplus")
        ax.set_xlabel("x")
        ax.set_ylabel("response")
        ax.set_title("A2I2 style: response curves")
        ax.legend(loc="lower right", frameon=False)
        fig.savefig(OUTDIR / "a2i2-response-curves.png")
        plt.close(fig)


def save_grouped_bars() -> None:
    categories = ["Baseline", "Model A", "Model B", "Model C"]
    acc = np.array([71.2, 76.8, 79.4, 81.1])
    f1 = np.array([68.4, 74.5, 77.8, 80.0])
    x = np.arange(len(categories))
    w = 0.38

    with plt.style.context(["a2i2", "no-latex"]):
        fig, ax = plt.subplots(figsize=(3.4, 2.6))
        ax.bar(x - w / 2, acc, width=w, label="Accuracy")
        ax.bar(x + w / 2, f1, width=w, label="F1 score")
        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=15, ha="right")
        ax.set_ylabel("Score (%)")
        ax.set_ylim(60, 85)
        ax.set_title("A2I2 style: benchmark summary")
        ax.legend(frameon=False)
        fig.savefig(OUTDIR / "a2i2-benchmark-bars.png")
        plt.close(fig)


if __name__ == "__main__":
    save_response_curve()
    save_grouped_bars()
