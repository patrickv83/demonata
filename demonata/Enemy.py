#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Character import Character

class Enemy(Character):
    def __init__(self, name, hp, weapon, *args):
        super(Enemy, self).__init__(name, hp, weapon)
        """@ReturnType Enemy"""
        self.___damage = args.pop
        """@AttributeType int"""
        self.___room = None
        # @AssociationType EnemyRoom
