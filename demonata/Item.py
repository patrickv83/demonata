#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Character

class Item(object):
	def __init__(self, aSelf, aName, aDesc, aValue):
		"""@ReturnType Item"""
		self.___name = None
		"""@AttributeType String"""
		self.___desc = None
		"""@AttributeType String"""
		self.___value = None
		"""@AttributeType int"""
		self._unnamed_Character_ = []
		# @AssociationType Character[]
		# @AssociationMultiplicity 1..*

	def __str__(self, aSelf):
		"""@ReturnType String"""
		pass

