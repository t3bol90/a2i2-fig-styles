"""Conference figure-size presets and style resolution helpers."""

from __future__ import annotations

import re
from typing import Dict, Tuple

_CONFERENCE_ALIASES = {
    "acl": "acl",
    "kdd": "kdd",
    "icdm": "icdm",
    "neurips": "neurips",
    "nips": "neurips",
}

_LAYOUT_ALIASES = {
    "1col": "1col",
    "onecol": "1col",
    "one-column": "1col",
    "2col": "2col",
    "twocol": "2col",
    "two-column": "2col",
}

_TYPE_ALIASES = {
    "line": "line",
    "bar": "bar",
    "scatter": "scatter",
    "heatmap": "heatmap",
    "image-grid": "image-grid",
    "imagegrid": "image-grid",
    "image": "image-grid",
    "text-equation": "text-equation",
    "textequation": "text-equation",
    "text": "text-equation",
    "equation": "text-equation",
}

_CONFERENCE_WIDTHS = {
    "acl": {"1col": 3.1, "2col": 6.3},
    "kdd": {"1col": 3.3, "2col": 6.8},
    "icdm": {"1col": 3.5, "2col": 7.2},
    "neurips": {"1col": 3.25, "2col": 6.75},
}

_TYPE_HEIGHTS = {
    "line": 2.3,
    "bar": 2.5,
    "scatter": 2.8,
    "heatmap": 2.9,
    "image-grid": 3.0,
    "text-equation": 2.0,
}


def _normalize_token(value: str) -> str:
    normalized = re.sub(r"[\s_]+", "-", value.strip().lower())
    return re.sub(r"-+", "-", normalized).strip("-")


def _canonical_conference(value: str) -> str:
    token = _normalize_token(value)
    if token not in _CONFERENCE_ALIASES:
        raise ValueError(f"Unknown conference '{value}'.")
    return _CONFERENCE_ALIASES[token]


def _canonical_layout(value: str) -> str:
    token = _normalize_token(value)
    if token not in _LAYOUT_ALIASES:
        raise ValueError(f"Unknown layout '{value}'.")
    return _LAYOUT_ALIASES[token]


def _canonical_figure_type(value: str) -> str:
    token = _normalize_token(value)
    if token not in _TYPE_ALIASES:
        raise ValueError(f"Unknown figure type '{value}'.")
    return _TYPE_ALIASES[token]


def _compose_name(conference: str, layout: str, figure_type: str) -> str:
    return f"{conference}-{layout}-{figure_type}"


PRESET_SPECS: Dict[str, Dict[str, object]] = {}
for _conference, _layouts in _CONFERENCE_WIDTHS.items():
    for _layout, _width in _layouts.items():
        for _figure_type, _height in _TYPE_HEIGHTS.items():
            _name = _compose_name(_conference, _layout, _figure_type)
            PRESET_SPECS[_name] = {
                "conference": _conference,
                "layout": _layout,
                "figure_type": _figure_type,
                "figsize": (_width, _height),
            }


def get_preset(conference: str, layout: str, figure_type: str) -> Dict[str, object]:
    """Return canonical style name and figsize for a preset combination."""
    canonical_conference = _canonical_conference(conference)
    canonical_layout = _canonical_layout(layout)
    canonical_figure_type = _canonical_figure_type(figure_type)
    name = _compose_name(
        canonical_conference, canonical_layout, canonical_figure_type
    )
    spec = PRESET_SPECS[name]
    return {
        "name": name,
        "conference": spec["conference"],
        "layout": spec["layout"],
        "figure_type": spec["figure_type"],
        "figsize": spec["figsize"],
    }


def resolve_preset_name(name: str) -> str:
    """Resolve canonical preset name from canonical or alias input."""
    token = _normalize_token(name)
    if token in PRESET_SPECS:
        return token

    parts = token.split("-")
    if len(parts) < 3:
        raise ValueError(f"Invalid preset name '{name}'.")

    conference = parts[0]
    remainder = parts[1:]
    if conference not in _CONFERENCE_ALIASES:
        raise ValueError(f"Invalid preset name '{name}'.")

    # conf-layout-type
    try:
        maybe_layout = remainder[0]
        figure_type = "-".join(remainder[1:])
        if maybe_layout and figure_type:
            spec = get_preset(conference, maybe_layout, figure_type)
            return str(spec["name"])
    except ValueError:
        pass

    # conf-type-layout
    try:
        maybe_layout = remainder[-1]
        figure_type = "-".join(remainder[:-1])
        if maybe_layout and figure_type:
            spec = get_preset(conference, maybe_layout, figure_type)
            return str(spec["name"])
    except ValueError as exc:
        raise ValueError(f"Invalid preset name '{name}'.") from exc

    raise ValueError(f"Invalid preset name '{name}'.")


def style_stack(
    conference: str, layout: str, figure_type: str, no_latex: bool = False
) -> list[str]:
    """Build a style stack for a conference figure preset."""
    preset = get_preset(conference, layout, figure_type)
    styles = ["science", str(preset["name"])]
    if no_latex:
        styles.append("no-latex")
    return styles
