#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Character import Character
from Weapon import Weapon
import random

class Enemy(Character):
    def __init__(self, name, hp, baseDamage = 5, weapon = None):
        """@ReturnType Enemy"""
        self.___room = None
        # @AssociationType EnemyRoom
        weapon = Weapon("Cudgel", "A basic bashing weapon", 0, 5) if weapon is None else weapon
        super(Enemy, self).__init__(name, hp, baseDamage, weapon)
