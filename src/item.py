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
        self._hidden = False

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

    def hide(self):
        """ Set the object to hidden """
        self._hidden = True

    def isHidden(self):
        """ Returns bool hidden state of item """
        return self._hidden

    def find(self):
        """ Set the object to not hidden """
        self._hidden = False

    def create(self):
        pass

    def __str__(self):
        """@ReturnType String"""
        return self._name
