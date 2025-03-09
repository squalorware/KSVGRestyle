# -*- coding: utf-8 -*-
from lxml.etree import XMLParser

from ksvg_restyle.cli.env import CmdEnv


def runtime_env() -> CmdEnv:
    return CmdEnv()


def xml_parser() -> XMLParser:
    return XMLParser(
        ns_clean=True,
        remove_blank_text=True,
        resolve_entities=True,
        load_dtd=True,
        huge_tree=True,
    )
