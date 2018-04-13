#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item import Item
from src.room import Room

class ArtifactRoom(Room):
    def __init__(self, x, y, item):
        self.item = item
        super(ArtifactRoom, self).__init__(x, y)

    def introText(self):
        #Print room description
        return

    def modifyPlayer(self, player):
        # Update player inventory with item
        return player

    def getCoordinates(self):
        return(self.x, self.y)
