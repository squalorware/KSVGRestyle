# -*- coding: utf-8 -*-
import click

from ksvg_restyle.handlers import load_color_theme, load_svg_image


@click.command()
@click.argument("svg", type=click.Path(exists=True), callback=load_svg_image)
@click.option(
    "-c",
    "--color-theme",
    required=True,
    type=click.Path(exists=True),
    callback=load_color_theme,
    help="Path to the Plasma Color Theme file",
)
@click.option(
    "-o",
    "--output",
    type=click.Path(exists=False),
    help="Output destination path (recolored SVG image)",
)
def main(svg, color_theme, output) -> None:
    click.echo(color_theme)


if __name__ == "__main__":
    main()
