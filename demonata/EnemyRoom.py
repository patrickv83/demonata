#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Enemy
import World
import Room

class EnemyRoom(Room):
	def __init__(self, aSelf, aX, aY, aEnemy):
		"""@ReturnType EnemyRoom"""
		self.___enemy = None
		"""@AttributeType Enemy"""
		self._unnamed_World_ = None
		# @AssociationType World
		self._unnamed_Enemy_ = None
		# @AssociationType Enemy
		# @AssociationKind Composition

	def modifyPlayer(self, aSelf, aPlayer):
		pass

