# -*- coding: utf-8 -*-
import click

from ksvg_restyle.handlers import load_color_theme
from ksvg_restyle.state import State


@click.command()
@click.argument("image", type=click.Path(exists=True))
@click.option(
    "-c",
    "--colour-theme",
    required=True,
    type=click.Path(exists=True),
    callback=load_color_theme,
)
@click.option("-o", "--output", type=click.Path(exists=False))
@click.pass_context
def main(ctx, image, colour_theme, output) -> None:
    ctx.obj = State(compressed=image, theme=colour_theme, out_path=output)
    click.echo(ctx.obj.theme)


if __name__ == "__main__":
    main()
