# -*- coding: utf-8 -*-
import re
import tomllib
from typing import Any, TextIO


def _clamp(value: int) -> int:
    return max(0, min(value, 255))


def _to_hex(rgb: str) -> str:
    red, green, blue = rgb.split(",")
    return "#{0:02x}{1:02x}{2:02x}".format(
        _clamp(int(red)),
        _clamp(int(green)),
        _clamp(int(blue)),
    )


def _str_literal(value: str) -> str:
    v = value.strip()
    # make sure boolean values are not stringified
    if v in ["true", "false"]:
        return v

    return '"{}"\n'.format(v)


def parse_color_theme(ct_file: TextIO) -> dict[str, Any]:
    """
    Read the KDE Plasma Color Theme stylesheet.

    Since its syntax is very close to TOML, patch content to make it valid TOML
    and then use tomllib to parse it and convert it to dict.
    :param ct_file: --- file contents (iostream)
    :return: a dict of colour theme styles
    """
    ct_str = ""
    re_header = r"^(\[\S+\])$"
    re_rgb = r"^\d+,\d+,\d+$"

    while line := ct_file.readline():
        if re.match(re_header, line):
            line = line.replace(":", ".")

        if "=" in line:
            k, v = line.split("=")
            val = v

            if re.match(re_rgb, v):
                val = _str_literal(_to_hex(v))

            if all(ch.isalpha() or ch.isspace() for ch in v):
                val = _str_literal(v)

            line = " = ".join([k, val])
        ct_str += line

    theme_dict = tomllib.loads(ct_str)
    return theme_dict
