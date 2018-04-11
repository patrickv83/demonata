#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item import Item
from src.room import Room
from src.character import Character

EAST = (1, 0)
WEST = (-1, 0)
SOUTH = (0, -1)
NORTH = (0, 1)

class Player(Character):
    def __init__(self, name, hp, baseDamage, inventory = list(), gold = 10, weapon = None, coords = (0,0)):
        """@ReturnType Player"""
        self.___inventory = inventory
        """@AttributeType Item*"""
        self.___gold = gold
        """@AttributeType Int"""
        #self.___room = Room(coords[0], coords[1])
        # @AssociationType Room
        self.___coords = coords
        super(Player, self).__init__(name, hp, baseDamage)

    def printInventory(self):
        """@ReturnType void"""
        pass

    def addItem(self, item):
        self.___inventory.append(item)

    def addGold(self, gold):
        """@ReturnType void"""
        self.___gold += gold

    def getGold(self):
        """@ReturnType int"""
        return self.___gold

    def setRoom(self, room):
        """@ReturnType void"""
        self.___room = room
        
    def getLocation(self):
        return self.___room.getCoords()

    def ___move(self, direction = []):
        coordList = list(self.___coords)
        x = coordList[0] + direction[0]
        y = coordList[1] + direction[1]
        self.___coords = (x,y)

    def move_north(self):
        self.___move(NORTH)

    def move_south(self):
        self.___move(SOUTH)

    def move_west(self):
        self.___move(WEST)

    def move_east(self):
        self.___move(EAST)
