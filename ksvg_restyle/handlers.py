# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Any

from click import BadParameter

from ksvg_restyle.parsers.svg import SvgImage, read_svg_file
from ksvg_restyle.parsers.theme import parse_color_theme


def load_svg_image(_, param: str, value: str) -> SvgImage:
    """Callback for click option decorator
    Reads the provided SVG file

    :return: a wrapper class representing an SVG image
    """
    file_path = Path(value)
    if file_path.is_file():
        if file_path.suffix not in [".svg", ".svgz", ".svg.gz"]:
            raise BadParameter(f"{param}: {value} - Unsupported file type")

        compressed = file_path.suffix in [".svgz", ".svg.gz"]

        return read_svg_file(compressed, file_path)
    else:
        raise BadParameter(f"{param}: {value} is not a file")


def load_color_theme(_, param: str, value: str) -> dict[str, Any]:
    """Callback for click.option decorator
    Reads the color theme stylesheet, then converts it to dict.

    :return: A dictionary containing the color theme definition
        with valid HTML-encoded values (CSS-compatible)
    """
    file_path = Path(value)
    if file_path.is_file():
        with open(value, "r", encoding="UTF-8") as f:
            try:
                colors = parse_color_theme(f)
            except ValueError as e:
                raise BadParameter(
                    message=f"{param}: Error reading color theme {value}:\n{e}"
                )
            else:
                return colors
    else:
        raise BadParameter(f"{param}: {value} is not a file")
