#!/usr/bin/python
# -*- coding: UTF-8 -*-
from item import Item
import random

class Weapon(Item):
    def __init__(self, name, desc, value, damage):
        """@ReturnType Weapon"""
        self.___damage = None
        """@AttributeType int"""
        super(Weapon, self).__init__(name, desc, value)

    def __str__(self):
        """@ReturnType String"""
        pass

    def attack(self):
        return random.randint(1, 1 + self.___damage)
