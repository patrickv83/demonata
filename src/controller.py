#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" The controller module """
import csv
import urwid

from src.view.main_view import GameView
from src.view.initial_view import InitialView
from src.player import Player
#from src.enemy_room import EnemyRoom
#from src.empty_room import EmptyRoom
#from src.artifact_room import ArtifactRoom

class Controller(object):
    """ The controller class - holds the map, instantiates the rooms, tracks the
        player and enemies """
    EAST = (1, 0)
    WEST = (-1, 0)
    SOUTH = (0, -1)
    NORTH = (0, 1)

    def __init__(self, startCoords=(0, 0)):
        """ Controller constructor
            New game: self._startinPosition = (0, 0)
            Load game: self._startingPosition = startCoords """

        self._player = Player("Patrick", 15, 10)
        self._playerLocation = startCoords
        """@AttributeType Tuple"""
        # @AssociationType Player
        # @AssociationKind Aggregation
        self._currentRoom = None
        self.loadFile('src/data/world.csv')

        self._gameView = GameView(self.getDescriptionText(), self.getMapText(),
                                  directions=self.getDirectionOptions(),
                                  actions=self.getActionOptions(),
                                  gameOpts=self.getGameOptions(),
                                  controller=self)

        self._initialView = InitialView(['New game', 'Load game', 'Exit'],
                                        self._gameView, game_loop=None)
        self._loop = urwid.MainLoop(self._initialView.screen,
                                    palette=[('reversed', 'standout', '')])
        self._initialView.set_game_loop(self._loop)


    def start(self):
        """ Start the main game loop """
        self._loop.run()

    def stop(self):
        """ Stop the main game loop """
        self._loop.stop()

    def loadFile(self, mapFile):
        """ReturnType void"""
        self.rooms = {}

        with open(mapFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                key = "{0}{1}".format(row.pop(0), row.pop(0))
                self.rooms.update({key: row})

    def getPlayerLocation(self):
        """ This method returns the player's current location as a tuple
            ReturnType tuple (x, y) """
        return self._playerLocation

    def getRooms(self):
        """ This method returns the loaded map. It is slated for removal very soon and should
            not be used """
        return self.rooms

    def getDescriptionText(self):
        """ This method gets the description text from the room at the player's current location
            ReturnType String """
        coords = self.getPlayerLocation()
        roomKey = "{}{}".format(coords[0], coords[1])
        return self.rooms[roomKey]

    def getMapText(self):
        """ This method returns a formatted string representation of the player's current location,
            nearby rooms, and direction arrows toward important locations
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

    def _canMove(self, direction):
        """ Checks if there is a room in <direction> from current room """
        x, y = self._playerLocation
        dirX, dirY = eval('Controller.{}'.format(direction))
        roomKey = '{}{}'.format(x + dirX, y + dirY)
        return roomKey in self.rooms

    def getDirectionOptions(self):
        """ This method builds the list of directions the player can move
            ReturnType list of strings """
        return ["Move {}".format(x).title() for x in ["NORTH", "SOUTH", "EAST", "WEST"]
                if self._canMove(x)]

    def getActionOptions(self):
        """ This method builds and returns the list of actions the player can take in the room
            ReturnType list of strings """

        options = ["Fight pixie", "Pick up whatsit", "Interrogate djinn"]
        return options

    def getGameOptions(self):
        """ This method returns the metagame options (e.g. Save, Load, Quit)
            ReturnType list of strings """
        options = ["Save", "Load", "Exit game"]
        return options

    def movePlayer(self, direction):
        """ This method updates the player's current location and instantiates a room if necessary
            ReturnType None """
        self._player.move(direction)
        self._playerLocation = self._player.getLocation()
        # if roomKey not in visitedRooms:
        #     self.generateRoom()

    def moveCallback(self, button):
        """ This method updates the gameView object every time the player moves """
        functions = {'move_north': (self.movePlayer, Controller.NORTH),
                     'move_south': (self.movePlayer, Controller.SOUTH),
                     'move_east': (self.movePlayer, Controller.EAST),
                     'move_west': (self.movePlayer, Controller.WEST)}
        label = button._w.original_widget.text.lower().replace(' ', '_')
        if label in functions:
            functions[label][0](functions[label][1])
        self._gameView.updateDescription(self.getDescriptionText())
        self._gameView.walker[0].contents[0] = \
           (self._gameView.createDirectionMenu(self.getDirectionOptions()), ('weight', 20, False))

    def optionCallback(self, button):
        """ This method updates the gameView object whenever the player uses the
            game options menu (save/load/quit/etc) """
        pass

    def actionCallback(self, button):
        """ This method updates the gameView object whenever the player performs an action from
            the action menu """
        pass
