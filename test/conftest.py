# -*- coding: utf-8 -*-
from pathlib import Path
from test import fixtures
from typing import Any, TextIO

import pytest
from lxml import etree

from ksvg_restyle.cli.env import CmdEnv
from ksvg_restyle.core.wrappers import ColorScheme, SvgImage

TEST_ROOT = Path(__file__).parent


# ----------------------------------------
# global (application-wide) fixture data
# ----------------------------------------
@pytest.fixture
def run_env() -> CmdEnv:
    return fixtures.general.runtime_env()


@pytest.fixture
def xml_parser() -> etree.XMLParser:
    return fixtures.general.xml_parser()


# ----------------------------------------
# color scheme/style-related fixture data
# ----------------------------------------
@pytest.fixture
def color_theme() -> TextIO:
    return fixtures.color_scheme.color_theme()


@pytest.fixture
def css_template() -> str:
    return fixtures.color_scheme.css_template()


@pytest.fixture
def old_colors() -> list[str]:
    return fixtures.color_scheme.old_colors()


@pytest.fixture
def plasma_colors() -> dict[str, Any]:
    return fixtures.color_scheme.plasma_colors()


@pytest.fixture
def cs_dict() -> dict[str, str]:
    return fixtures.color_scheme.cs_dict()


@pytest.fixture
def color_scheme() -> ColorScheme:
    return fixtures.color_scheme.color_scheme()


# ----------------------------------------
#        SVG and XML fixture data
# ----------------------------------------
@pytest.fixture
def xmlns() -> dict[str, str]:
    return fixtures.svg.xmlns_dict()


@pytest.fixture
def svg_string() -> str:
    return fixtures.svg.svg_string()


@pytest.fixture
def svg_etree() -> etree.ElementTree:
    return fixtures.svg.svg_etree()


@pytest.fixture
def svg_compressed() -> SvgImage:
    path = TEST_ROOT / "fixtures" / "data" / "svg" / "background.svgz"
    return fixtures.svg.svg_compressed(path)


@pytest.fixture
def svg_uncompressed() -> SvgImage:
    path = TEST_ROOT / "fixtures" / "data" / "svg" / "background.svg"
    return fixtures.svg.svg_uncompressed(path)


@pytest.fixture
def xslt_template() -> str:
    return fixtures.svg.xslt_template()


@pytest.fixture
def styled_svg() -> str:
    return fixtures.svg.styled_svg()


@pytest.fixture
def styled_svg_bytes() -> bytes:
    return fixtures.svg.styled_svg_bytes()


@pytest.fixture
def styled_svg_string() -> str:
    return fixtures.svg.styled_svg_string()


@pytest.fixture
def transformed_svg() -> etree.ElementTree:
    return fixtures.svg.transformed_svg_etree()


@pytest.fixture
def transformed_svg_string() -> str:
    return fixtures.svg.transformed_svg_string()
