# -*- coding: utf-8 -*-
import unittest

import pytest

import ksvg_restyle.core.parsers.theme as theme_parser


class TestColorThemeParser(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, color_theme, color_scheme):
        self.ct_file = color_theme
        self.color_scheme = color_scheme

    def test_clamp(self) -> None:
        """
        Test that the clamp method works as expected.
        Ensure that rgb values are always within the 0-255 range.
        """
        # Test regular value
        expected = 69
        actual = theme_parser._clamp(69)
        self.assertEqual(actual, expected)
        # Test max value
        expected = 255
        actual = theme_parser._clamp(255)
        self.assertEqual(actual, expected)
        # Test upper out-of-bounds value
        expected = 255
        actual = theme_parser._clamp(420)
        self.assertNotEqual(420, actual)
        self.assertEqual(actual, expected)
        # Test min value
        expected = 0
        actual = theme_parser._clamp(0)
        self.assertEqual(actual, expected)
        # Test lower out-of-bounds value
        expected = 0
        actual = theme_parser._clamp(-69)
        self.assertNotEqual(69, actual)
        self.assertEqual(actual, expected)

    def test_to_hex(self) -> None:
        """
        Test proper conversion from (R,G,B) to HTML hexadecimal color value.
        """
        expected = "#000000"
        actual = theme_parser._to_hex("0,0,0")
        self.assertEqual(actual, expected)
        expected = "#ffffff"
        actual = theme_parser._to_hex("255, 255, 255")
        self.assertEqual(actual, expected)
        expected = "#ff8045"
        actual = theme_parser._to_hex("255,128,69")
        self.assertEqual(actual, expected)

    def test_parse_color_theme(self) -> None:
        expected = self.color_scheme
        actual = theme_parser.parse_color_theme(self.ct_file)
        self.assertDictEqual(actual.data, expected.data)
