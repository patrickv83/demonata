from abc import ABCMeta, abstractmethod

class Room():
    __metaclass__ = ABCMeta
    """This is the Room abstract class"""

    @abstractmethod
    def __init__(self, description):
        self.description = description

    @abstractmethod
    def generateDescription(self):
        self.description = "Nothing to see here"

    @abstractmethod
    def printDescription(self):
        print self.description
