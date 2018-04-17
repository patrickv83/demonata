#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item import Item
from src.character import Character

class Player(Character):
    def __init__(self, name, hp, baseDamage, inventory = list(), gold = 10, weapon = None, coords = (0,0)):
        """@ReturnType Player"""
        self._inventory = inventory
        """@AttributeType Item*"""
        self._gold = gold
        """@AttributeType Int"""
        # @AssociationType Room
        self._coords = coords
        super(Player, self).__init__(name, hp, baseDamage)

    def printInventory(self):
        """@ReturnType void"""
        pass

    def addItem(self, item):
        self._inventory.append(item)

    def addGold(self, gold):
        """@ReturnType void"""
        self._gold += gold

    def getGold(self):
        """@ReturnType int"""
        return self._gold

    def setRoom(self, room):
        """@ReturnType void"""
        self._room = room
        
    def getLocation(self):
        return self._room.getCoords()

    def _move(self, direction = []):
        coordList = list(self._coords)
        x = coordList[0] + direction[0]
        y = coordList[1] + direction[1]
        self._coords = (x,y)

    def move_north(self):
        self._move(NORTH)

    def move_south(self):
        self._move(SOUTH)

    def move_west(self):
        self._move(WEST)

    def move_east(self):
        self._move(EAST)
