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
        styled_svg,
        styled_svg_string,
        svg_etree,
        transformed_svg_string,
        xml_parser,
        xmlns,
        xslt_template,
    ):
        self.color_scheme = color_scheme
        self.css = css_template
        self.namespaces = xmlns
        self.old_colors = old_colors
        self.styled = styled_svg
        self.styled_str = styled_svg_string
        self.svg = svg_etree
        self.transformed = transformed_svg_string
        self.xml_parser = xml_parser
        self.xslt = xslt_template

    def test_find_or_add_style(self):
        styled, old_colors = builder.find_or_add_style(
            nsmap=self.namespaces,
            svg=self.svg,
            template=self.css,
            xml_parser=self.xml_parser,
        )
        self.assertListEqual(old_colors, self.old_colors)
        self.assertXMLEqual(
            expected=etree.tostring(styled).decode("utf-8"),
            actual=self.styled_str,
        )

    def test_apply_stylesheet(self):
        result = builder.apply_stylesheet(
            color_scheme=self.color_scheme,
            nsmap=self.namespaces,
            old_colors=self.old_colors,
            svg=self.styled,
            template=self.xslt,
            xml_parser=self.xml_parser,
        )
        self.assertXMLEqual(
            actual=etree.tostring(result).decode("utf-8"),
            expected=self.transformed,
        )
