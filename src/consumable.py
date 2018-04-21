""" Consumable Module
    Defines the Consumable superclass
    Defines each Consumable subclass
    Defines an enumerated list of Enemy Types (CT) """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from enum import Enum
from src.item import Item

# Enumeration for Consumables
class CT(Enum):
    """ Enumerated list of Consumable Types (CT) """
    MOLDY_BREAD = 1
    BREAD = 2
    APPLE = 3
    SNICKERS = 4
    HONEY_GLAZED_HAM = 5

class Consumable(Item):
    """ Consumable superclass creates a consumable """
    def __init__(self, name, desc, value, uses, consumableType):
        """@ReturnType Consumable"""
        self.uses = uses
        self.name = name
        self.consumableType = consumableType
        """@AttributeType int"""
        super(Consumable, self).__init__(name, desc, value)

    def getUses(self):
        """ Get the number of times the consumable can be used. """
        return self.uses

    def getName(self):
        """ Get the name of the consumable. """
        return self.name
    
    def setName(self, name):
        """@ReturnType Void - sets consumable name"""
        self.name = name

    def consume(self):
        """ When the consumable is consumed, this method must be called.
        This will decrease the number of uses the consumable has. """
        self.uses = self.getUses() - 1

    def getValue(self):
        """ Get the value of the consumable.  If the consumable has
        no uses left, this will return 0. """
        if self.getUses() == 0:
            return 0
        return self.appraise()

    def __str__(self):
        """@ReturnType String"""
        return "Name: {0}\nUses: {1}\nValue: {2}".format(self.name, self.uses, self._value)

class MoldyBread(Consumable):
    """Moldy bread causes damage"""
    def __init__(self):
        super(MoldyBread, self).__init__(name="Moldy Bread",
                                         desc="A disgusting piece of moldy bread.",
                                         value=-5, uses=2, consumableType=CT.MOLDY_BREAD)

class Bread(Consumable):
    """Bread heals a small amount"""
    def __init__(self):
        super(Bread, self).__init__(name="Bread",
                                    desc="A square piece of white bread.",
                                    value=5, uses=2, consumableType=CT.BREAD)

# Yummy Apples
class Apple(Consumable):
    """Apples heal slightly more than bread"""
    def __init__(self):
        super(Apple, self).__init__(name="Apple",
                                    desc="A pink lady apple of exquisite flavor.",
                                    value=25, uses=5, consumableType=CT.APPLE)

class Snickers(Consumable):
    """Snickers satisfies you"""
    def __init__(self):
        super(Snickers, self).__init__(name="Snickers",
                                       desc="You're not yourself when you're hungry.",
                                       value=75, uses=3, consumableType=CT.SNICKERS)

class HoneyGlazedHam(Consumable):
    """A whole ham will last a long time"""
    def __init__(self):
        super(HoneyGlazedHam, self).__init__(name="Honey Glazed Ham",
                                             desc="A large spiral cut honey glazed ham.",
                                             value=150, uses=25, consumableType=CT.HONEY_GLAZED_HAM)
