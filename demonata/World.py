#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Player
import EnemyRoom
import EmptyRoom
import ArtifactRoom
import Start

class World(object):
	def loadRooms(self):
		pass

	def __init__(self):
		self.___startingPosition = None
		"""@AttributeType Tuple"""
		self._unnamed_Player_ = None
		# @AssociationType Player
		# @AssociationKind Aggregation
		self._unnamed_EnemyRoom_ = None
		# @AssociationType EnemyRoom
		# @AssociationKind Aggregation
		self._unnamed_EmptyRoom_ = None
		# @AssociationType EmptyRoom
		# @AssociationKind Aggregation
		self._unnamed_ArtifactRoom_ = None
		# @AssociationType ArtifactRoom
		# @AssociationKind Aggregation
		self._unnamed_Start_ = None
		# @AssociationType Start
		# @AssociationKind Aggregation

