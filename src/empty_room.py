#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.room import Room

class EmptyRoom(Room):
	# EmptyRoom constructor
    def __init__(self, x, y):
        super().__init__(x, y)
	
	# introText displays the room description
	def introText(self):
		return
		
	# modifyPlayer
	# Empty room has no player modification
	def modifyPlayer(self, player):
		pass

	# Postcondition: Returns room's coordinates in the form of a tuple
    def getCoordinates(self):
        return (self.x, self.y)
