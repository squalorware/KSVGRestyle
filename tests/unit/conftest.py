# -*- coding: utf-8 -*-
import io
from typing import TextIO

import pytest

from tests.mock_files import loader


@pytest.fixture
def color_theme() -> str:
    with open(
        file=loader.get_mock_file("theme.colors"), mode="r", encoding="UTF-8"
    ) as theme:
        return theme.read()


@pytest.fixture
def color_theme_short() -> TextIO:
    theme = """[General]
ColorScheme=CustomTheme
Name=Custom Theme
shadeSortColumn=true

[ColorEffects:Disabled]
Color=146,145,144
ColorAmount=0
ColorEffect=0
ContrastAmount=0.65
ContrastEffect=1
IntensityAmount=0.1
IntensityEffect=2
"""
    return io.StringIO(theme)


@pytest.fixture
def color_theme_short_dict() -> dict:
    return {
        "General": {
            "ColorScheme": "CustomTheme",
            "Name": "Custom Theme",
            "shadeSortColumn": True,
        },
        "ColorEffects": {
            "Disabled": {
                "Color": "#929190",
                "ColorAmount": 0,
                "ColorEffect": 0,
                "ContrastAmount": 0.65,
                "ContrastEffect": 1,
                "IntensityAmount": 0.1,
                "IntensityEffect": 2,
            }
        },
    }
