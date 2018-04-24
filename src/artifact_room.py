""" artifact room module """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.factory import Factory
from src.room import Room

class ArtifactRoom(Room):
    """ ArtifactRoom class - a room type that has a random item in it """
    def __init__(self, x, y, text, item=None):
        self.item = item or self.randomItem
        super(ArtifactRoom, self).__init__(x, y, text)

    def randomItem(self):
        """ method returns a random item, using the itemFactory method
            Precondition: None
            Postcondition: returns random Item """
        return Factory.itemFactory()
