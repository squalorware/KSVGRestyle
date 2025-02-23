# -*- coding: utf-8 -*-
import gzip
from pathlib import Path


class SvgImage:
    """
    SvgImage class. - A wrapper around a svg image.

    Attributes:
        path -- Path to the svg image.
        compressed -- Whether the svg image is compressed.
        xml -- XML representation of the svg image.
    """

    def __init__(self, compressed: bool, path: Path, xml: str):
        self.compressed = compressed
        self.path = path
        self.xml = xml


def read_svg_file(compressed: bool, path: Path) -> SvgImage:
    if compressed:
        f = gzip.open(path, "rb")
    else:
        f = open(path, "rb")
    xml = f.read().decode("utf-8")
    f.close()

    return SvgImage(compressed, path, xml)
