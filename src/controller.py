#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" The controller module """
import csv
from sys import exit as exitGame
import dill
from urwid import MainLoop


from src.view.main_view import GameView
from src.view.initial_view import InitialView
from src.player import Player
#from src.tutorial_room import TutorialRoom, Office
#from src.enemy_room import EnemyRoom
from src.room import Room
#from src.artifact_room import ArtifactRoom
from src.room_factory import roomFactory

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
        self._room = None
        self.map = None
        self._currentRoom = None
        self.loadFile('src/data/world.csv')
        self._roomKey = self.getRoomKey()
        self._visited = {'00': Room(0, 0, self.map['00'][1]),
                         '01': Room(0, 0, self.map['01'][1]),
                         '02': Room(0, 0, self.map['02'][1]),
                         '03': Room(0, 0, self.map['03'][1])}

        self._gameView = GameView(self.getDescriptionText(), self.getMapText(),
                                  directions=self.getDirectionOptions(),
                                  actions=self.getActionOptions(),
                                  gameOpts=self.getGameOptions(),
                                  controller=self)

        self._initialView = InitialView(['New game', 'Load game', 'Exit'],
                                        self._gameView, game_loop=None)
        self._loop = MainLoop(self._initialView.screen,
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
        self.map = {}

        with open(mapFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                key = "{0}{1}".format(row.pop(0), row.pop(0))
                roomTitle = row.pop(0)
                self.map.update({key: [roomTitle, row]})

    def getPlayerLocation(self):
        """ This method returns the player's current location as a tuple
            ReturnType tuple (x, y) """
        return self._playerLocation

    def getRoomKey(self):
        """ This method generates a key for the map based on the player's current location
            @ReturnType String """
        return '{}{}'.format(self._playerLocation[0], self._playerLocation[1])

    def getRooms(self):
        """ This method returns the loaded map. It is slated for removal very soon and should
            not be used
            @ReturnType dict """
        return self.map

    def getDescriptionText(self):
        """ This method gets the description text from the room at the player's current location
            @ReturnType String """
        return self._visited[self._roomKey].getText()

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
        dirX, dirY = eval('Controller.{}'.format(direction))
        roomKey = '{}{}'.format(self._playerLocation[0] + dirX,
                                self._playerLocation[1] + dirY)
        return roomKey in self.map

    def getDirectionOptions(self):
        """ This method builds the list of directions the player can move
            ReturnType list of Strings """
        return ["Move {}".format(x).title() for x in ["NORTH", "SOUTH", "EAST", "WEST"]
                if self._canMove(x)]

    def getActionOptions(self):
        """ This method builds and returns the list of actions the player can take in the room
            ReturnType list of Strings """

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
        self._roomKey = self.getRoomKey()
        try:
            self._room = self._visited[self._roomKey]
        except KeyError:
            self._room = roomFactory(self._playerLocation[0],
                                     self._playerLocation[1],
                                     self.map[self._roomKey][1])
    def updateGameView(self):
        self._gameView.updateDescription(self.getDescriptionText())
        self._gameView.walker[0].contents[0] = \
           (self._gameView.createDirectionMenu(self.getDirectionOptions()), ('weight', 20, False))

    def moveCallback(self, button):
        """ This method updates the gameView object every time the player moves """
        functions = {'move_north': (self.movePlayer, Controller.NORTH),
                     'move_south': (self.movePlayer, Controller.SOUTH),
                     'move_east': (self.movePlayer, Controller.EAST),
                     'move_west': (self.movePlayer, Controller.WEST)}
        label = button._w.original_widget.text.lower().replace(' ', '_')
        try:
            functions[label][0](functions[label][1])
        except KeyError:
            return
        self.updateGameView()

    def optionCallback(self, button):
        """ This method updates the gameView object whenever the player uses the
            game options menu (save/load/quit/etc) """
        functions = {'save': self.saveGame,
                     'load': self.loadGame,
                     'exit_game': exitGame}
        label = button._w.original_widget.text.lower().replace(' ', '_')
        try:
            functions[label]()
        except KeyError:
            pass

    def actionCallback(self, button):
        """ This method updates the gameView object whenever the player performs an action from
            the action menu """
        functions = {'pick_up': self._player.addItem}

    def saveGame(self):
        """ This method pickles the controller (self) and player (self._player) to save the current
            game state
            @ReturnType None """
        with open('saves/patrick_001', 'w+') as f:
            dill.dump(self._player, f)
            dill.dump(self._playerLocation, f)
            dill.dump(self._currentRoom, f)
            dill.dump(self.map, f)
            dill.dump(self._visited, f)
            dill.dump(self._roomKey, f)

    def loadGame(self):
        """ This method unpickles the controller (self) and player (self._player) to load the
            saved game state
            @ReturnType None """
        with open('saves/patrick_001') as f:
            self._player = dill.load(f)
            self._playerLocation = dill.load(f)
            self._currentRoom = dill.load(f)
            self.map = dill.load(f)
            self._visited = dill.load(f)
            self._roomKey = dill.load(f)
            self.updateGameView()
