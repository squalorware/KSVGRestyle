# -*- coding: utf-8 -*-
import unittest

import pytest

from ksvg_restyle.parsers.theme import (
    _clamp,
    _to_hex,
    parse_color_theme,
)


class ColorThemeParserTestCase(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, color_theme, color_theme_dict):
        self.ct_str = color_theme
        self.ct_dict = color_theme_dict

    def test_clamp(self) -> None:
        """
        Test that the clamp method works as expected.
        Ensure that rgb values are always within the 0-255 range.
        """
        # Test regular value
        expected = 69
        actual = _clamp(69)
        assert actual == expected
        # Test max value
        expected = 255
        actual = _clamp(255)
        assert actual == expected
        # Test upper out-of-bounds value
        expected = 255
        actual = _clamp(420)
        assert actual != 420
        assert actual == expected
        # Test min value
        expected = 0
        actual = _clamp(0)
        assert actual == expected
        # Test lower out-of-bounds value
        expected = 0
        actual = _clamp(-69)
        assert actual != -69
        assert actual == expected

    def test_to_hex(self) -> None:
        """
        Test proper conversion from (R,G,B) to HTML hexadecimal color value.
        """
        expected = "#000000"
        actual = _to_hex("0,0,0")
        assert actual == expected
        expected = "#ffffff"
        actual = _to_hex("255, 255, 255")
        assert actual == expected
        expected = "#ff8045"
        actual = _to_hex("255,128,69")
        assert actual == expected

    def test_parse_color_theme(self) -> None:
        """
        Test that the parse_color_theme function works as expected.
        Should transform a KDE Plasma Color Theme to a Python dict.
        :param ct_str: fixture: conftest:color_theme_short() returns color theme
        :param ct_dict: fixture: conftest:color_theme_dict() returns parsed dict
        """
        expected = self.ct_dict
        actual = parse_color_theme(self.ct_str)
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
