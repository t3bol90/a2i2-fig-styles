"""Tests for deterministic figure dimensions in conference presets."""

import itertools

from scienceplots import get_preset


WIDTHS = {
    "acl": {"1col": 3.1, "2col": 6.3},
    "kdd": {"1col": 3.3, "2col": 6.8},
    "icdm": {"1col": 3.5, "2col": 7.2},
    "neurips": {"1col": 3.25, "2col": 6.75},
}

HEIGHTS = {
    "line": 2.3,
    "bar": 2.5,
    "scatter": 2.8,
    "heatmap": 2.9,
    "image-grid": 3.0,
    "text-equation": 2.0,
}


def test_dimensions_exact_match():
    for conference, layouts in WIDTHS.items():
        for layout, width in layouts.items():
            for figure_type, height in HEIGHTS.items():
                preset = get_preset(conference, layout, figure_type)
                assert preset["figsize"] == (width, height)


def test_height_is_shared_by_figure_type_across_conferences():
    layouts = ("1col", "2col")
    for figure_type, expected_height in HEIGHTS.items():
        for layout in layouts:
            heights = []
            for conference in WIDTHS:
                preset = get_preset(conference, layout, figure_type)
                _, height = preset["figsize"]
                heights.append(height)
            assert heights == [expected_height] * len(WIDTHS)


def test_width_changes_with_layout_for_each_conference():
    figure_types = list(HEIGHTS.keys())
    for conference, figure_type in itertools.product(WIDTHS.keys(), figure_types):
        preset_1col = get_preset(conference, "1col", figure_type)
        preset_2col = get_preset(conference, "2col", figure_type)
        width_1col, _ = preset_1col["figsize"]
        width_2col, _ = preset_2col["figsize"]
        assert width_1col < width_2col

