#!/usr/bin/python
# -*- coding: UTF-8 -*-
import World
import Room

class EmptyRoom(Room):
	def introText(self, aSelf):
		"""@ReturnType void"""
		pass

	def modifyPlayer(self, aSelf, aPlayer):
		"""@ReturnType void"""
		pass

	def operation(self):
		pass

	def __init__(self):
		self._unnamed_World_ = None
		# @AssociationType World

