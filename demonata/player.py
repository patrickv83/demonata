#!/usr/bin/python
""" The demonata Player class. Extends the character class with gold and coordinates"""
# -*- coding: UTF-8 -*-
from demonata.character import Character

EAST = (1, 0)
WEST = (-1, 0)
SOUTH = (0, -1)
NORTH = (0, 1)

class Player(Character):
    def __init__(self, *args, **kwargs):
        coords = kwargs.pop('coords', (0, 0))      # coords is an (x, y) tuple
        inventory = kwargs.pop('inventory', list())
        gold = kwargs.pop('gold', 10)
        """@ReturnType Player"""
        self._inventory = inventory
        """@AttributeType Item*"""
        self._gold = gold
        """@AttributeType Int"""
        self._room = Room(coords[0], coords[1])
        # @AssociationType Room
        self._coords = coords
        super(Player, self).__init__(*args)

    def print_inventory(self):
        """@ReturnType void"""
        pass

    def add_item(self, item):
        self._inventory.append(item)

    def add_gold(self, gold):
        """@ReturnType void"""
        self._gold += gold

    def get_gold(self):
        """@ReturnType int"""
        return self._gold

    def set_room(self, room):
        """@ReturnType void"""
        self._room = room

    def get_location(self):
        return self._room.getCoords()

    def _move(self, direction):
        coord_list = list(self._coords)
        x = coord_list[0] + direction[0]
        y = coord_list[1] + direction[1]
        self._coords = (x, y)

    def move_north(self):
        self._move(NORTH)

    def move_south(self):
        self._move(SOUTH)

    def move_west(self):
        self._move(WEST)

    def move_east(self):
        self._move(EAST)
