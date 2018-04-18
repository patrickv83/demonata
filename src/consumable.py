#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item import Item
from enum import Enum

# Enumeration for Consumables
class ConsumableType(Enum):
    MOLDY_BREAD = 1
    BREAD = 2
    APPLE = 3
    SNICKERS = 4
    HONEY_GLAZED_HAM = 5
    
class Consumable(Item):
    def __init__(self, name, desc, value, uses, consumableType):
        """@ReturnType Consumable"""
        self.___uses = uses
        self.___name = name
        self.___consumableType = consumableType
        """@AttributeType int"""
        super(Consumable, self).__init__(name, desc, value)

    def getUses(self):
        return self.___uses

    def getName(self):
        return self.___name
    
    def consume(self):
        self.___uses = self.getUses() - 1
        
    def getValue(self):
        if(self.getUses() == 0):
            return 0;
        return self.getValue()

    def __str__(self):
        """@ReturnType String"""
        return "Name: {0}\nUses: {1}\nValue: {2}".format(self.___name, self.___uses, self.___value)

# Moldy Bread causes damage
class MoldyBread(Consumable):
    def __init__(self):
        super(MoldyBread, self).__init__(name="Moldy Bread", desc="A disgusting piece of moldy bread." value=-5, uses=2, consumableType=1)
        
# Bread heals a small amount
class Bread(Consumable):
    def __init__(self):
        super(Bread, self).__init__(name="Bread", desc="A square piece of white bread." value=5, uses=2, consumableType=2)

# Yummy Apples
class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__(name="Apple", desc="A pink lady apple of exquisite flavor." value=25, uses=5, consumableType=3)
        
class Snickers(Consumable):
    def __init__(self):
        super(Snickers, self).__init__(name="Snickers", desc="You're not yourself when you're hungry." value=75, uses=3, consumableType=4)
        
class HoneyGlazedHam(Consumable):
    def __init__(self):
        super(HoneyGlazedHam, self).__init__(name="Honey Glazed Ham", desc="A large spiral cut honey glazed ham." value=150, uses=25, consumableType=5)