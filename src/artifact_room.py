#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item import Item
from src.room import Room

class ArtifactRoom(Room):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

	def introText(self):
		# print room description
		return

    def modifyPlayer(self, player):
		# update player inventory with item found in room 
        return player
		
	def getCoordinates(self):
		return(self.x, self.y)

