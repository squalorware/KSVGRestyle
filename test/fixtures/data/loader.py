# -*- coding: utf-8 -*-
from pathlib import Path


def datafile(short_path: str) -> Path:
    """
    Resolves a path to a mock file.
    :param short_path: short path to data file
    """
    return Path(__file__).parent / short_path
