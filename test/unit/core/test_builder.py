# -*- coding: utf-8 -*-
from test.base import BaseXMLTestCase

import pytest
from lxml import etree

from ksvg_restyle.core import builder


class TestSVGBuilder(BaseXMLTestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(
        self,
        color_scheme,
        css_template,
        old_colors,
        styled_svg_string,
        svg_etree,
        xml_parser,
        xmlns,
    ):
        self.color_scheme = color_scheme
        self.css = css_template
        self.namespaces = xmlns
        self.old_colors = old_colors
        self.styled = styled_svg_string
        self.svg = svg_etree
        self.xml_parser = xml_parser

    def test_find_or_add_style_no_style_tag(self):
        styled, old_colors = builder.find_or_add_style(
            nsmap=self.namespaces,
            svg=self.svg,
            template=self.css,
            xml_parser=self.xml_parser,
        )
        self.assertSetEqual(old_colors, self.old_colors)
        self.assertXMLEqual(etree.tostring(styled).decode("utf-8"), self.styled)
