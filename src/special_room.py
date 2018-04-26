""" Special Room
    Tutorial Room
    Bar
    Bookstore
    Grocery Store """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.room import Room
from src.npc import *

class TutorialRoom(Room):
    """ Tutorial room to teach investigation """
    def __init__(self, x, y, text):
        self.tutor = Tutor()
        super(TutorialRoom, self).__init__(x, y, text)

    def modifyPlayer(self, player):
        # Player interaction - interrogation
        pass

class Bar(Room):
    """ Bar - Special Room """
    def __init__(self, x, y, text):
        self.bartender = Bartender()
        super(Bar, self).__init__(x, y, text)

    def modifyPlayer(self, player):
        # Player interaction - interrogation
        pass

class Bookstore(Room):
    """ Bookstore - special room """
    def __init__(self, x, y, text):
        self.bookworm = Bookworm()
        super(Bookstore, self).__init__(x, y, text)

    def modifyPlayer(self, player):
        # Player interaction - interrogation
        pass

class GroceryStore(Room):
    """ GroceryStore - special room """
    def __init__(self, x, y, text):
        self.cashier = Cashier()
        super(GroceryStore, self).__init__(x, y, text)

    def modifyPlayer(self, player):
        # Player interaction - interrogation
        pass
