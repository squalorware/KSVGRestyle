# -*- coding: utf-8 -*-
import click


# from .console import run
@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename) -> None:
    print(filename)
