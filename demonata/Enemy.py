#!/usr/bin/python
# -*- coding: UTF-8 -*-
import EnemyRoom
import Character

class Enemy(Character):
	def __init__(self, aSelf, aName, aHp, aDamage):
		"""@ReturnType Enemy"""
		self.___damage = None
		"""@AttributeType int"""
		self._unnamed_EnemyRoom_ = None
		# @AssociationType EnemyRoom

