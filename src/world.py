#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import system
from src.player import Player
from src.enemy_room import EnemyRoom
from src.empty_room import EmptyRoom
from src.artifact_room import ArtifactRoom

import csv

class World(object):
    def __init__(self, startCoords=(0, 0)):
        """ World constructor
            New game: self._startinPosition = (0, 0)
            Load game: self._startingPosition = startCoords """
        self._startingPosition = startCoords
        """@AttributeType Tuple"""
        self._player = None
        # @AssociationType Player
        # @AssociationKind Aggregation
        self._currentRoom = None
        self.loadFile('src/data/world.csv')

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

    def getDescriptionText(self):
        """ This method gets the description text from the room at the player's current location
            ReturnType String """
        return self.rooms['00']

    def getMapText(self):
        """ This method returns a formatted string representation of the player's current location, nearby
            rooms, and direction arrows toward important locations
            Something like this (border lines for illustration):
                                    ______________________________________
                                   |                                      |
                                   |                                      |
                                   | <--- grocery                         |
                                   |                                      |
                                   |                                      |
                                   |                                      |
                                   |    (street)      X      (street)     |
                                   |                                      |
                                   | <--- bar              office         |
                                   |                         |            |
                                   |                         |            |
                                   |                         v            |
                                   |______________________________________| """

        return """<- grocery

                  street  o  street

                  <- bar      """
 
    def getMenuOptions(self):
        """ This method builds the list of actions the player can take, including move <direction>,
            search room, pick up item, fight enemy, question witness, etc 
            ReturnType list of strings"""
        return ["Move north", "Pick up revolver", "Question bar patron", "Beat up pixie"]


