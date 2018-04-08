#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Item(object):
    def __init__(self, name, desc, value):
        """@ReturnType Item"""
        self.___name = name
        """@AttributeType String"""
        self.___desc = desc
        """@AttributeType String"""
        self.___value = value
        """@AttributeType int"""

    def appraise(self):
        return self.___value

    def describe(self):
        return self.___desc

    def identity(self):
        return self.___name
    
    def __str__(self):
        """@ReturnType String"""
        pass
