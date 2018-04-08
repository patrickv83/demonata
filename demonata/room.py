#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Room(object):
    def __init__(self, x, y):
        """@ReturnType Room"""
        self.___x = x
        """@AttributeType int"""
        self.___y = y
        """@AttributeType int"""

    def generateDescription(self):
        """@ReturnType void
        This method generates a description based on the location, items and
        enemies. Not implemented yet."""
        pass

    def modifyPlayer(self, player):
        """@ReturnType void"""
        pass

    def getCoords(self):
        return (self.___x, self.___y)
