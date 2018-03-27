#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Item
import World
import Character

class Player(Character):
	def __init__(self, aSelf, aName, aHp, aInventory, aGold):
		"""@ReturnType Player"""
		self.___inventory = None
		"""@AttributeType Item*"""
		self.___gold = None
		"""@AttributeType Int"""
		self._unnamed_World_ = None
		# @AssociationType World

	def printInvetory(self):
		"""@ReturnType void"""
		pass

	def setGold(self, aSelf):
		"""@ReturnType void"""
		pass

	def getGold(self, aSelf):
		"""@ReturnType int"""
		pass

