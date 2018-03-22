from abc import ABCMeta, abstractmethod

class Item():
    __metaclass__ = ABCMeta
    """This is the Item abstract class"""

    @abstractmethod
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
