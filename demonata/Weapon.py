#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Item import Item
import random

class Weapon(Item):
    def __init__(self, name, desc, value, damage):
        """@ReturnType Weapon"""
        self.___damage = damage
        self.___name = name
        """@AttributeType int"""
        super(Weapon, self).__init__(name, desc, value)

    def getDamage(self):
        return self.___damage

    def getName(self):
        return self.___name

    def __str__(self):
        """@ReturnType String"""
        return "Name: {0}\nDamage: {1}\nValue: {2}".format(self.___name, self.___damage, self.___value)
