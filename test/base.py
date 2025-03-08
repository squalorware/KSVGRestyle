# -*- coding: utf-8 -*-
from doctest import Example
from unittest import TestCase

from lxml.doctestcompare import PARSE_XML, LXMLOutputChecker


class BaseXMLTestCase(TestCase):
    def assertXMLEqual(self, actual, expected):
        checker = LXMLOutputChecker()
        if not checker.check_output(expected, actual, PARSE_XML):
            msg = checker.output_difference(
                example=Example("", expected), got=actual, optionflags=PARSE_XML
            )
            raise AssertionError(msg)
