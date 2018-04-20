#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" The player module """
from src.character import Character

class Player(Character):
<<<<<<< HEAD
    def __init__(self, name, hp, inventory = list(), gold = 10, weapon = None, coords = (0, 0)):
=======
    """ Player class, tracks location, HP, equipment/inventory, gold, etc """
    EAST = (1, 0)
    WEST = (-1, 0)
    SOUTH = (0, -1)
    NORTH = (0, 1)

    def __init__(self, name, hp, baseDamage, inventory=None, gold=10, weapon=None, coords=(0, 0)):
>>>>>>> refs/remotes/origin/master
        """@ReturnType Player"""
        self._inventory = inventory or []
        """@AttributeType Item*"""
        self._gold = gold
        """@AttributeType Int"""
<<<<<<< HEAD
        self.___weapon = weapon
        #self.___room = Room(coords[0], coords[1])
        # @AssociationType Room
        self.___coords = coords
        super(Player, self).__init__(name, hp)
=======
        # @AssociationType Room
        self._coords = coords
        super(Player, self).__init__(name, hp, baseDamage)
>>>>>>> refs/remotes/origin/master

    def printInventory(self):
        """@ReturnType void"""
        pass

    def addItem(self, item):
        """ Add Item <item> to player's inventory
            @ReturnType void"""
        self._inventory.append(item)

    def addGold(self, gold):
        """@ReturnType void"""
        self._gold += gold

    def getGold(self):
        """@ReturnType int"""
        return self._gold

<<<<<<< HEAD
#    def setRoom(self, room):
#        """@ReturnType void"""
#        self.___room = room

    def getLocation(self):
        return self.___room.getCoords()

    def ___move(self, direction = []):
        coordList = list(self.___coords)
        x = coordList[0] + direction[0]
        y = coordList[1] + direction[1]
        self.___coords = (x, y)

    def move_north(self):
        self.___move(NORTH)

    def move_south(self):
        self.___move(SOUTH)

    def move_west(self):
        self.___move(WEST)

    def move_east(self):
        self.___move(EAST)
=======
    def getLocation(self):
        """ Get player's current location
            @ReturnType int,int tuple """
        return self._coords

    def move(self, direction=()):
        """ Update player's current location
            @ReturnType void"""
        self._coords = (self._coords[0] + direction[0],
                        self._coords[1] + direction[1])
>>>>>>> refs/remotes/origin/master
