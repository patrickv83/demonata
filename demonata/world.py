#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Player import Player
from EnemyRoom import EnemyRoom
from EmptyRoom import EmptyRoom
from ArtifactRoom import ArtifactRoom
from Start import Start
import csv

class World(object):
    def loadFile(self, file):
        """ReturnType void"""
        self.rooms = {}

        with open(file) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                id = "{0}{1}".format(row.pop(0), row.pop(0))
                self.rooms.update({id: row})

    def getRooms(self):
        return self.rooms

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
        self.loadFile('data/world.csv')
