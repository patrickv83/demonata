#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" The player module """
import logging
from random import randint
from src.character import Character
from src.weapon import Weapon

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
        self._weapon = weapon or Weapon.create()
        self._coords = coords
        super(Player, self).__init__(name, hp)

    def getInventory(self):
        """ Returns player's inventory """
        return self._inventory

    def addItem(self, item):
        """ Add Item <item> to player's inventory
            @ReturnType void"""
        if not item.isHidden():
            self._inventory.append(item)
            logging.debug("Added item %s to inventory. Inventory now %s", 
                          item.identify(), self._inventory)

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

    def fight(self, enemy):
        """ Fight an enemy
            :param enemy: the enemy to fight"""
        while not (self.isDead() or enemy.isDead()):
            try:
                enemy.takeDamage(self._weapon.getDamage())
            except AttributeError:
                enemy.takeDamage(randint(1, 5))
            self.takeDamage(enemy.damage)

    def interrogate(self, character):
        """ Interrogate an NPC
            :param character: the non-player character to interrogate """
        pass

    def move(self, direction):
        """ Update player's current location
            @ReturnType void"""
        self._coords = (self._coords[0] + direction[0],
                        self._coords[1] + direction[1])
