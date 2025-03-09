# -*- coding: utf-8 -*-
import io
import json
from test.fixtures.data import datafile
from typing import Any, TextIO

from ksvg_restyle.core.wrappers import ColorScheme


def color_theme() -> TextIO:
    with open(datafile("color_scheme/theme.colors.in"), "r") as theme:
        content = theme.read()
        return io.StringIO(content)


def css_template() -> str:
    with open(datafile("color_scheme/style.css.in"), "r") as stylesheet:
        css = stylesheet.read()
        return css


def old_colors() -> list[str]:
    return [
        "#666666",
        "#c7d6e6",
        "#dedede",
        "#ffffff",
        "#b6b6b6",
        "#909090",
        "#d4d4d4",
        "#008000",
        "#000000",
    ]


def plasma_colors() -> dict[str, Any]:
    with open(datafile("color_scheme/colors.json.in"), "r") as f:
        colors = json.load(f)
        return colors


def cs_dict() -> dict[str, str]:
    return {
        "Text": "#ffffff",
        "Background": "#101010",
        "Highlight": "#4e7598",
        "ViewText": "#ffffff",
        "ViewBackground": "#000000",
        "ViewHover": "#4e7598",
        "ViewFocus": "#4e7598",
        "ButtonText": "#ffffff",
        "ButtonBackground": "#1c1e22",
        "ButtonHover": "#4e7598",
        "ButtonFocus": "#4e7598",
    }


def color_scheme() -> ColorScheme:
    return ColorScheme(plasma_colors())
