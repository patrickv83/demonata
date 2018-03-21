from abc import ABCMeta, abstractmethod

class Room():
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


