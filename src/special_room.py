""" Special Room
    Tutorial Room
    Bar
    Bookstore
    Grocery Store """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.room import Room
from src.artifact_room import SearchRoom
from src.npc import *
from item import Item

#class TutorialRoom(Room):
#    """ Tutorial room to teach investigation """
#    def __init__(self, x, y, text):
#        self.character = Landlord()
#        super(TutorialRoom, self).__init__(x, y, text)

#    def modifyPlayer(self, player):
#        # Player interaction - interrogation
#        pass

class Bar(Room):
    """ Bar - Special Room """
    def __init__(self, x, y, text):
        self.bartender = Bartender()
        super(Bar, self).__init__(x, y, text)

    def modifyPlayer(self, player):
        # Player interaction - interrogation
        pass

class Bookstore(SearchRoom):
    """ Bookstore - special room """
    def __init__(self, x, y, text):
        self.bookworm = Bookworm()
        super(Bookstore, self).__init__(x, y, text, item=Item(name="A sharp pencil",
                                                              desc="A Ticonderoga #2, the cadillac of pencils",
                                                              value=3))
        self.item.find()

    def modifyPlayer(self, player):
        # Player interaction - interrogation
        player.addItem(Item(name="Advanced Demon Summoning", 
                            desc="Bound in human flesh and inked with human blood", 
                            value=500))

class GroceryStore(Room):
    """ GroceryStore - special room """
    def __init__(self, x, y, text):
        self.cashier = Cashier()
        super(GroceryStore, self).__init__(x, y, text)

    def modifyPlayer(self, player):
        # Player interaction - interrogation
        pass
