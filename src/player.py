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

    def __init__(self, name, hp, inventory=None, gold=10, weapon=None, coords=(0, 0)):
        """@ReturnType Player"""
        self._inventory = inventory or []
        """@AttributeType Item*"""
        self._gold = gold
        """@AttributeType Int"""
        self._weapon = weapon
        #self._room = Room(coords[0], coords[1])
        # @AssociationType Room
        self._coords = coords
        super(Player, self).__init__(name, hp)

    def getInventory(self):
        """ Returns player's inventory """
        return self._inventory

    def addItem(self, item):
        """ Add Item <item> to player's inventory
            @ReturnType void"""
        self._inventory.append(item)

    def consume(self, consumable):
        """ Consume an item.  Dead players can't consume items.
            @ReturnType void"""
        if self.isDead():
            return
        self.heal(consumable.getValue())
        consumable.consume()
        if consumable.getUses() == 0:
            self._inventory.remove(consumable)

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

    def move(self, direction):
        """ Update player's current location
            @ReturnType void"""
        self._coords = (self._coords[0] + direction[0],
                        self._coords[1] + direction[1])
