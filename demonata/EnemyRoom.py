#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Enemy import Enemy
from Room import Room

class EnemyRoom(Room):
    def __init__(self, x, y, enemy):
        """@ReturnType EnemyRoom"""
        self.___enemy = enemy
        """@AttributeType Enemy"""
