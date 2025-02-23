# -*- coding: utf-8 -*-
import unittest
from pathlib import Path

import pytest

from ksvg_restyle.parsers.svg import read_svg_file


class SvgParserTestCase(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, svg_object):
        self.svg = svg_object

    def test_read_svg_file(self):
        test_root = Path(__file__).parent.parent
        file_path = test_root / "mock_files" / "share" / "background.svgz"
        expected = self.svg
        actual = read_svg_file(compressed=True, path=file_path)
        assert expected.compressed == actual.compressed
        assert expected.path == actual.path
        assert expected.xml == actual.xml
