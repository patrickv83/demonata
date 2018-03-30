#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Item

class Character(object):
	def isDead(self, aSelf):
		"""@ReturnType boolean"""
		return self.hp <= 0

	def __init__(self, aSelf, aName, aHp):
		"""@ReturnType Character"""
		self.name = None
		"""@AttributeType String"""
		self.hp = None
		"""@AttributeType Int"""
		self.unnamed_Item_ = None
		# @AssociationType Item

