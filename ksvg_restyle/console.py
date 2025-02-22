# -*- coding: utf-8 -*-
import click

from ksvg_restyle.handlers.theme_parser import parse_color_theme


@click.command()
@click.option(
    "-c", "--colour-theme", required=True, type=click.Path(exists=True)
)
@click.argument("filename", type=click.Path(exists=True))
def main(colour_theme, filename) -> None:
    with open(colour_theme, "r", encoding="UTF-8") as f:
        theme = parse_color_theme(f)
    print(theme)


if __name__ == "__main__":
    main()
