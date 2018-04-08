<<<<<<< HEAD
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
=======
from abc import ABCMeta, abstractmethod

class Room:
    __metaclass__ = ABCMeta
    """This is the Room abstract class"""

    @abstractmethod
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description

    @abstractmethod
    def getCoordinates(self):
        return x,y

    @abstractmethod
    def generateDescription(self):
        self.description = "Nothing to see here"

    @abstractmethod
    def getDescription(self):
        print self.description


class EmptyRoom(Room):
    """This is the EmptyRoom class"""

    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description

    def getCoordinates(self):
        return self.x, self.y

    def generateDescription(self):
        """TODO: Generate description based on contents and location of room"""
        self.description = "Random placeholder room description"

    def getDescription(self):
        return self.description


>>>>>>> 7061933bd0ef710a36586030d9ae3d52685c4f4d
