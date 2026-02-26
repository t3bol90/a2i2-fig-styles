# a2i2-fig-styles

Acknowledgment: This package is built on top of the excellent SciencePlots work by John Garrett and contributors.

`a2i2-fig-styles` provides publication-ready Matplotlib style presets for:
- `a2i2`
- `acl`, `kdd`, `icdm`, `neurips`
- `1col` and `2col` layouts
- figure types: `line`, `bar`, `scatter`, `heatmap`, `image-grid`, `text-equation`

## Install

```bash
pip install -e .
```

## Quick Start

```python
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(["science", "neurips-1col-line", "no-latex"])
plt.plot([0, 1, 2], [0.2, 0.7, 0.9])
plt.xlabel("Epoch")
plt.ylabel("Score")
plt.show()
```

For `a2i2`:

```python
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(["a2i2", "no-latex"])
```

## Preset API

```python
from scienceplots import get_preset, resolve_preset_name, style_stack

preset = get_preset("neurips", "1col", "line")
print(preset["name"], preset["figsize"])  # neurips-1col-line, (3.25, 2.3)

print(resolve_preset_name("nips_line_1col"))  # neurips-1col-line

styles = style_stack("acl", "2col", "image-grid", no_latex=True)
```

## Generate Example Figures

Run all example scripts:

```bash
PYTHONPATH=src python3 examples/plot-a2i2-examples.py
PYTHONPATH=src python3 examples/plot-conference-presets.py
PYTHONPATH=src python3 examples/plot-all-preset-gallery.py
```

Outputs are saved in `examples/figures/`.

## Rendered Examples

### A2I2

![A2I2 response curves](examples/figures/a2i2-response-curves.png)
![A2I2 benchmark bars](examples/figures/a2i2-benchmark-bars.png)

### Conference Presets

![NeurIPS 1col line](examples/figures/preset-neurips-1col-line.png)
![ACL 2col bar](examples/figures/preset-acl-2col-bar.png)
![KDD 1col scatter](examples/figures/preset-kdd-1col-scatter.png)
![ICDM 2col heatmap](examples/figures/preset-icdm-2col-heatmap.png)
![NeurIPS 2col image-grid](examples/figures/preset-neurips-2col-image-grid.png)
![ACL 1col text-equation](examples/figures/preset-acl-1col-text-equation.png)

### Full Style Catalog Samples

![A2I2 catalog](examples/figures/style-preview-a2i2.png)
![NeurIPS 2col line catalog](examples/figures/style-preview-neurips-2col-line.png)
![ACL 1col heatmap catalog](examples/figures/style-preview-acl-1col-heatmap.png)
![KDD 2col text-equation catalog](examples/figures/style-preview-kdd-2col-text-equation.png)

## Common Use Cases

- LLM training curves: `neurips-1col-line`, `acl-1col-line`
- CV/vision panels: `neurips-2col-image-grid`, `icdm-2col-image-grid`
- Benchmark comparison bars: `kdd-2col-bar`, `acl-2col-bar`
- Confusion matrix/attention map: `neurips-1col-heatmap`, `icdm-1col-heatmap`
- Equation-heavy explanatory figures: `acl-1col-text-equation`, `kdd-1col-text-equation`

## Test

```bash
python3 -m pytest -q
```
