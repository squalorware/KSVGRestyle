# -*- coding: utf-8 -*-
import gzip
import io
from pathlib import Path
from typing import TextIO

import pytest

from ksvg_restyle.parsers.svg import SvgImage
from tests.mock_files import loader

TEST_ROOT = Path(__file__).parent.parent


@pytest.fixture
def color_theme() -> TextIO:
    with open(file=loader.get_mock_file("theme.colors"), mode="r") as theme:
        content = theme.read()
        return io.StringIO(content)


@pytest.fixture
def color_theme_dict() -> dict:
    return {
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


@pytest.fixture
def svg_object() -> SvgImage:
    with gzip.open(loader.get_mock_file("background.svgz"), "rb") as f:
        xml = f.read().decode("utf-8")

    path = TEST_ROOT / "mock_files" / "share" / "background.svgz"
    return SvgImage(compressed=True, path=path, xml=xml)
