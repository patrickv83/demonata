#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.enemy import Enemy
from src.room import Room

class EnemyRoom(Room):

	# EnemyRoom constructor
    def __init__(self, x, y, enemy):
        self.enemy = enemy
		super().__init__(self, x, y)
		
	# introText prints room description
	def introText(self):
		return
	
	# modifyPlayer
	def modifyPlayer(self, player):
		# Update player with results of enemy interaction
		return player
	
	# Postcondition: returns room coordinates
	def getCoordinates(self):
		return (self.x, self.y)
