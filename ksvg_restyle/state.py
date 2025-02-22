# -*- coding: utf-8 -*-
class State(object):
    def __init__(self, **kwargs):
        self.compressed = kwargs.get("compressed", True)
        self.theme = kwargs.get("theme", {})
        self.out_path = kwargs.get("out_path", "")
