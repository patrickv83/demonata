""" artifact room module """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
from random import randint
from src.factory import Factory
from src.room import Room

class ArtifactRoom(Room):
    """ ArtifactRoom class - a room type that has a random item in it """
    def __init__(self, x, y, text, item=None):
        self.item = item or self.randomItem()
        super(ArtifactRoom, self).__init__(x, y, text)

    def randomItem(self):
        """ method returns a random item, using the itemFactory method
            Precondition: None
            Postcondition: returns random Item """
        return Factory.itemFactory().create()

    def removeItem(self):
        self.item = None

    def getItem(self):
        return self.item



class SearchRoom(ArtifactRoom):
    """ SearchRoom - Room with hidden object in it
        Precondition: Takes and x and y coordinate tuple (type int) for the location
        Postcondition: Returns a room """
    def __init__(self, x, y, text, item=None):
        super(SearchRoom, self).__init__(x, y, text, item)
        self.item.hide()

    def search(self):
        """ search method - search room, player has 40% chance of finding item
            Precondition: None
            Postcondition: Returns whether player found item (type bool)"""
        searchRoll = randint(1, 100)
        logging.debug("Search roll: %s", searchRoll)
        return (searchRoll > 40)
