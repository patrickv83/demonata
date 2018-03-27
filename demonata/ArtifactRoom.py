#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Item
import World
import Room

class ArtifactRoom(Room):
	def __init__(self, aSelf, aX, aY, aItem):
		"""@ReturnType Artifact Room"""
		self.___item = None
		"""@AttributeType Item"""
		self._unnamed_World_ = None
		# @AssociationType World

	def addArtifact(self, aSelf, aPlayer):
		"""@ReturnType void"""
		pass

	def modifyPlayer(self, aSelf, aPlayer):
		pass

