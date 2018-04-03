#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Character import Character

class Enemy(Character):
    def __init__(self, name, hp, *args):
        super(Enemy, self).__init__(name, hp)
        """@ReturnType Enemy"""
        self.___damage = args.pop
        """@AttributeType int"""
        self.___room = EnemyRoom()
        # @AssociationType EnemyRoom
