# -*- coding: utf-8 -*-
import gzip
from pathlib import Path
from test.fixtures.data import datafile
from test.fixtures.general import xml_parser

from lxml import etree

from ksvg_restyle.core.wrappers import SvgImage


def xmlns_dict() -> dict[str, str]:
    return {
        "_": "http://www.w3.org/2000/svg",
        "cc": "http://creativecommons.org/ns#",
        "dc": "http://purl.org/dc/elements/1.1/",
        "inkscape": "http://www.inkscape.org/namespaces/inkscape",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
        "svg": "http://www.w3.org/2000/svg",
        "xlink": "http://www.w3.org/1999/xlink",
    }


def svg_string() -> str:
    with open(datafile("svg/background.svg"), "r") as img:
        svg = img.read()
        return svg


def svg_etree() -> etree.ElementTree:
    with open(datafile("svg/background.svg"), "rb") as img:
        svg = etree.fromstring(img.read(), parser=xml_parser())
        return svg


def svg_compressed(path: Path) -> SvgImage:
    with gzip.open(datafile("svg/background.svgz"), "rb") as img:
        xml = etree.fromstring(img.read(), parser=xml_parser())
        return SvgImage(path=path, xml=xml)


def svg_uncompressed(path: Path) -> SvgImage:
    with open(datafile("svg/background.svg"), "rb") as img:
        xml = etree.fromstring(img.read(), parser=xml_parser())
        return SvgImage(path=path, xml=xml)


def xslt_template() -> str:
    with open(datafile("general/transform.xsl.in"), "r") as f:
        template = f.read()
        return template


def styled_svg() -> etree.ElementTree:
    with open(datafile("general/styled.xml.out"), "rb") as img:
        styled = etree.fromstring(img.read(), parser=xml_parser())
        return styled


def styled_svg_bytes() -> bytes:
    with open(datafile("general/styled.xml.out"), "rb") as img:
        styled = img.read()
        return bytes(styled)


def styled_svg_string() -> str:
    with open(datafile("general/styled.xml.out"), "r") as img:
        styled = img.read()
        return styled


def transformed_svg_etree() -> etree.ElementTree:
    xslt = etree.XML(xslt_template())
    transform = etree.XSLT(xslt)
    return transform(styled_svg())


def transformed_svg_string() -> str:
    with open(datafile("svg/transformed.xml.out"), "r") as img:
        transformed = img.read()
        return transformed
