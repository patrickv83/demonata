#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Item(object):
    def __init__(self, name=None, desc=None, value=5):
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

    def identify(self):
        return self._name

    def create(self):
        pass

    def __str__(self):
        """@ReturnType String"""
        return self._name

