"""Item Module"""
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
        """For getting item value
        @ReturnType int"""
        return self._value

    def describe(self):
        """For getting item description
        @ReturnType String"""
        return self._desc

    def identify(self):
        """For getting item name
        @ReturnType String"""
        return self._name

    def setName(self, name):
        """For setting item name
        @ReturnType String"""
        self._name = name

    def create(self):
        pass

    def __str__(self):
        """@ReturnType String"""
        return self._name
