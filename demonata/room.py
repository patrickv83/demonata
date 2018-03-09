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
    def printDescription(self):
        print self.description
