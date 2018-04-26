#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Item(object):
    def __init__(self, name, desc, value):
        """@ReturnType Item"""
        self._name = name
        """@AttributeType String"""
        self._desc = desc
        """@AttributeType String"""
        self._value = value
        """@AttributeType int"""
        
    def appraise(self):
        return self._value

    def describe(self):
        return self._desc

    def identity(self):
        return self._name

    def setName(self, name):
        self._name = name

    def __str__(self):
        """@ReturnType String"""
        pass

