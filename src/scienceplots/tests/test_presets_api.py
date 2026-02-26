"""Tests for conference preset helper API."""

import pytest

from scienceplots import PRESET_SPECS, get_preset, resolve_preset_name, style_stack


def test_preset_count():
    assert len(PRESET_SPECS) == 48


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("neurips-1col-line", "neurips-1col-line"),
        ("nips-1col-line", "neurips-1col-line"),
        ("neurips-line-1col", "neurips-1col-line"),
        ("NeurIPS_1col_line", "neurips-1col-line"),
        ("acl-image-grid-2col", "acl-2col-image-grid"),
        ("acl-2col-image-grid", "acl-2col-image-grid"),
        ("icdm-text-equation-1col", "icdm-1col-text-equation"),
    ],
)
def test_resolve_preset_aliases(name, expected):
    assert resolve_preset_name(name) == expected


@pytest.mark.parametrize(
    ("conference", "layout", "figure_type", "expected"),
    [
        ("ACL", "1col", "line", "acl-1col-line"),
        ("nips", "2col", "bar", "neurips-2col-bar"),
        ("kdd", "two-column", "heatmap", "kdd-2col-heatmap"),
        ("icdm", "onecol", "image", "icdm-1col-image-grid"),
        ("neurips", "2col", "textequation", "neurips-2col-text-equation"),
    ],
)
def test_get_preset_normalization(conference, layout, figure_type, expected):
    preset = get_preset(conference, layout, figure_type)
    assert preset["name"] == expected


@pytest.mark.parametrize(
    ("conference", "layout", "figure_type"),
    [
        ("foo", "1col", "line"),
        ("acl", "3col", "line"),
        ("acl", "1col", "unknown"),
    ],
)
def test_get_preset_invalid_inputs(conference, layout, figure_type):
    with pytest.raises(ValueError):
        get_preset(conference, layout, figure_type)


def test_style_stack_with_and_without_no_latex():
    assert style_stack("acl", "1col", "line") == ["science", "acl-1col-line"]
    assert style_stack("acl", "1col", "line", no_latex=True) == [
        "science",
        "acl-1col-line",
        "no-latex",
    ]

