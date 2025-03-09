# -*- coding: utf-8 -*-
import unittest
from test.conftest import TEST_ROOT

import pytest

from ksvg_restyle.core import wrappers


class TestWrappers(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, cs_dict, plasma_colors, svg_etree, xmlns):
        self.nsmap = xmlns
        self.plasma_theme = plasma_colors
        self.scheme = cs_dict
        self.xml = svg_etree

    def test_svg_image(self):
        compressed = TEST_ROOT / "fixtures" / "data" / "svg" / "background.svgz"
        wrapper_instance = wrappers.SvgImage(compressed, self.xml)
        self.assertIsInstance(wrapper_instance, wrappers.SvgImage)
        self.assertEqual(wrapper_instance.location, compressed.parent)
        self.assertEqual(wrapper_instance.filename, compressed.stem)
        self.assertTrue(wrapper_instance.compressed)
        self.assertDictEqual(wrapper_instance.xmlns, self.nsmap)

        uncomp = TEST_ROOT / "fixtures" / "data" / "svg" / "background.svg"
        wrapper_instance = wrappers.SvgImage(uncomp, self.xml)
        self.assertIsInstance(wrapper_instance, wrappers.SvgImage)
        self.assertFalse(wrapper_instance.compressed)

    def test_color_scheme(self):
        color_scheme = wrappers.ColorScheme(self.plasma_theme)
        self.assertIsInstance(color_scheme, wrappers.ColorScheme)
        self.assertDictEqual(color_scheme.data, self.scheme)
