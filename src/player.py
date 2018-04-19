#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" The player module """
from src.character import Character

class Player(Character):
    """ Player class, tracks location, HP, equipment/inventory, gold, etc """
    EAST = (1, 0)
    WEST = (-1, 0)
    SOUTH = (0, -1)
    NORTH = (0, 1)

    def __init__(self, name, hp, baseDamage, inventory=None, gold=10, weapon=None, coords=(0, 0)):
        """@ReturnType Player"""
        self._inventory = inventory or []
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
        """ Add Item <item> to player's inventory
            @ReturnType void"""
        self._inventory.append(item)

    def addGold(self, gold):
        """@ReturnType void"""
        self._gold += gold

    def getGold(self):
        """@ReturnType int"""
        return self._gold

    def getLocation(self):
        """ Get player's current location
            @ReturnType int,int tuple """
        return self._coords

    def move(self, direction=()):
        """ Update player's current location
            @ReturnType void"""
        self._coords = (self._coords[0] + direction[0],
                        self._coords[1] + direction[1])
