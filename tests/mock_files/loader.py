# -*- coding: utf-8 -*-
from pathlib import Path


def get_mock_file(filename: str) -> Path:
    """
    Resolves a path to a mock file.
    :param filename: mock file name
    """
    return Path(__file__).parent / "share" / filename
