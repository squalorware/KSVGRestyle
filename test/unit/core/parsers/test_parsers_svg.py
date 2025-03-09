# -*- coding: utf-8 -*-
import unittest
from test.conftest import TEST_ROOT

import pytest
from lxml import etree

import ksvg_restyle.core.parsers.svg as svg_parser


class TestSVGParser(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(
        self,
        svg_compressed,
        svg_uncompressed,
        transformed_svg,
        xml_parser,
        xslt_template,
    ):
        self.svgz = svg_compressed
        self.svg = svg_uncompressed
        self.transformed = transformed_svg
        self.xml_parser = xml_parser
        self.xslt = xslt_template

    def test_parse_svg_compressed(self):
        file_path = TEST_ROOT / "fixtures" / "data" / "svg" / "background.svgz"
        expected = self.svgz
        actual = svg_parser.parse_svg(file_path, self.xml_parser)
        self.assertEqual(actual.filename, expected.filename)
        self.assertEqual(actual.location, expected.location)
        self.assertEqual(actual.compressed, expected.compressed)

    def test_parse_svg_uncompressed(self):
        file_path = TEST_ROOT / "fixtures" / "data" / "svg" / "background.svg"
        expected = self.svg
        actual = svg_parser.parse_svg(file_path, self.xml_parser)
        self.assertEqual(actual.filename, expected.filename)
        self.assertEqual(actual.location, expected.location)
        self.assertEqual(actual.compressed, expected.compressed)

    def test_create_copy(self):
        expected = etree.tostring(self.svg.data).decode("utf-8")
        actual = svg_parser.create_copy(self.svg.data, self.xml_parser)
        self.assertEqual(etree.tostring(actual).decode("utf-8"), expected)

    def test_transform_svg(self):
        expected = etree.tostring(self.transformed).decode("utf-8")
        actual = svg_parser.transform_svg(
            svg=self.transformed, template=self.xslt, xml_parser=self.xml_parser
        )
        self.assertEqual(etree.tostring(actual).decode("utf-8"), expected)
