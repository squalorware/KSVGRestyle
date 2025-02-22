# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Any

from click import BadParameter, make_pass_decorator

from ksvg_restyle.parsers.theme import parse_color_theme
from ksvg_restyle.state import State

pass_state = make_pass_decorator(State, ensure=True)


@pass_state
def load_color_theme(state: State, _, param: str, value: str) -> dict[str, Any]:
    """Callback for click.option decorator
    Reads the color theme stylesheet, then converts it to dict.

    :return: A dictionary containing the color theme definition
        with valid HTML-encoded values (CSS-compatible)
    """
    file_path = Path(value)
    if file_path.is_file():
        with open(value, "r", encoding="UTF-8") as f:
            try:
                state.theme = parse_color_theme(f)
            except ValueError as e:
                raise BadParameter(
                    message=f"{param}: Error reading color theme {value}:\n{e}"
                )
            else:
                return state.theme
    else:
        raise BadParameter(f"{param}: {value} is not a file")
