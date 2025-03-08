# -*- coding: utf-8 -*-
import io
from test.fixtures.data import datafile
from typing import TextIO

from ksvg_restyle.core.wrappers import ColorScheme


def color_theme() -> TextIO:
    with open(datafile("color_scheme/theme.colors.in"), "r") as theme:
        content = theme.read()
        return io.StringIO(content)


def css_template() -> str:
    with open(datafile("color_scheme/style.css.in"), "r") as stylesheet:
        css = stylesheet.read()
        return css


def old_colors() -> set[str]:
    return {
        "#ffffff",
        "#d4d4d4",
        "#909090",
        "#008000",
        "#c7d6e6",
        "#666666",
        "#000000",
        "#dedede",
        "#b6b6b6",
    }


def color_scheme() -> ColorScheme:
    return ColorScheme(
        {
            "Button": {
                "BackgroundAlternate": "#222221",
                "BackgroundNormal": "#1c1e22",
                "DecorationFocus": "#4e7598",
                "DecorationHover": "#4e7598",
                "ForegroundActive": "#810061",
                "ForegroundInactive": "#747474",
                "ForegroundLink": "#1010ff",
                "ForegroundNegative": "#fc4040",
                "ForegroundNeutral": "#ffd052",
                "ForegroundNormal": "#ffffff",
                "ForegroundPositive": "#91ffb9",
                "ForegroundVisited": "#ae7483",
            },
            "Selection": {
                "BackgroundAlternate": "#3379bb",
                "BackgroundNormal": "#4e7598",
                "DecorationFocus": "#4e7598",
                "DecorationHover": "#4e7598",
                "ForegroundActive": "#810061",
                "ForegroundInactive": "#747474",
                "ForegroundLink": "#1010ff",
                "ForegroundNegative": "#f16363",
                "ForegroundNeutral": "#ffdd00",
                "ForegroundNormal": "#000000",
                "ForegroundPositive": "#007f00",
                "ForegroundVisited": "#ae7483",
            },
            "Tooltip": {
                "BackgroundAlternate": "#001c3b",
                "BackgroundNormal": "#232300",
                "DecorationFocus": "#4e7598",
                "DecorationHover": "#4e7598",
                "ForegroundActive": "#810061",
                "ForegroundInactive": "#747474",
                "ForegroundLink": "#1010ff",
                "ForegroundNegative": "#fc4040",
                "ForegroundNeutral": "#ffd052",
                "ForegroundNormal": "#ffffff",
                "ForegroundPositive": "#91ffb9",
                "ForegroundVisited": "#ae7483",
            },
            "View": {
                "BackgroundAlternate": "#090807",
                "BackgroundNormal": "#000000",
                "DecorationFocus": "#4e7598",
                "DecorationHover": "#4e7598",
                "ForegroundActive": "#810061",
                "ForegroundInactive": "#747474",
                "ForegroundLink": "#1010ff",
                "ForegroundNegative": "#fc4040",
                "ForegroundNeutral": "#ffd052",
                "ForegroundNormal": "#ffffff",
                "ForegroundPositive": "#91ffb9",
                "ForegroundVisited": "#ae7483",
            },
            "Window": {
                "BackgroundAlternate": "#272625",
                "BackgroundNormal": "#101010",
                "DecorationFocus": "#4e7598",
                "DecorationHover": "#4e7598",
                "ForegroundActive": "#810061",
                "ForegroundInactive": "#747474",
                "ForegroundLink": "#1010ff",
                "ForegroundNegative": "#fc4040",
                "ForegroundNeutral": "#ffd052",
                "ForegroundNormal": "#ffffff",
                "ForegroundPositive": "#91ffb9",
                "ForegroundVisited": "#ae7483",
            },
        }
    )
