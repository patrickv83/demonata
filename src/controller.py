#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" The controller module """
import csv
from sys import exit as exitGame
from os import makedirs
import errno

import logging
import dill
from urwid import MainLoop

from src.view.main_view import GameView
from src.view.initial_view import InitialView
from src.player import Player
from src.room import Room
from src.artifact_room import SearchRoom
from src.special_room import TutorialRoom, Bar, Bookstore, GroceryStore
from src.factory import Factory


logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class Controller(object):
    """ The controller class - holds the map, instantiates the rooms, tracks the
        player and enemies """
    DIRECTIONS = {'EAST': (1, 0), 'WEST': (-1, 0), 'SOUTH': (0, -1), 'NORTH': (0, 1)}

    def __init__(self, startCoords=(0, 0)):
        """ Controller constructor
            New game: self._startinPosition = (0, 0)
            Load game: self._startingPosition = startCoords """

        self._saveDir = 'saves'
        self._player = Player("Patrick", 15, gold=100)
        self._playerLocation = startCoords
        self._room = None
        self.map = None
        self._currentRoom = None
        self.loadFile('src/data/world.csv')
        self._roomKey = self.getRoomKey()
        # Preseed _visited dict with special rooms
        self._visited = {'00': Room(0, 0, self.map['00'][1]),         # Office
                         '01': SearchRoom(0, 1, self.map['01'][1]),         # Search
                         '02': TutorialRoom(0, 2, self.map['02'][1]), # Interrogate
                         '03': Room(0, 3, self.map['03'][1]),         # Combat
                         '-55': Bookstore(-5, 5, self.map['-55'][1]),      # Bookstore
                         '-312': GroceryStore(-3, 12, self.map['-312'][1]),   # Grocery
                         '110': Bar(1, 10, self.map['110'][1]),      # Bar
                         '615': Room(6, 15, self.map['615'][1])       # Apartment
                        }

        self._gameView = GameView(self.getDescriptionText(), self.getStatText(),
                                  directions=self.getDirectionOptions(),
                                  actions=self.getActionOptions(),
                                  gameOpts=self.getGameOptions(),
                                  controller=self)

        self._initialView = InitialView(['New game', 'Load game', 'Exit'],
                                        self._gameView, game_loop=None, controller=self)
        self._loop = MainLoop(self._initialView.screen,
                              palette=[('reversed', 'standout', '')])
        self._initialView.set_game_loop(self._loop)


    def start(self):
        """ Start the main game loop """
        logging.info('Game started')
        self._loop.run()

    def stop(self):
        """ Stop the main game loop """
        self._loop.stop()

    def loadFile(self, mapFile):
        """ReturnType void"""
        self.map = {}

        with open(mapFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile, delimiter='|')
            for row in csvReader:
                key = "{0}{1}".format(row.pop(0), row.pop(0))
                roomTitle = row.pop(0)
                self.map.update({key: [roomTitle, row]})
        logging.debug(str(self.map))

    def getPlayerLocation(self):
        """ Returns the player's current location as a tuple
            ReturnType tuple (x, y) """
        logging.debug('Accessing Controller._playerLocation: %s', self._playerLocation)
        return self._playerLocation

    def getRoomKey(self):
        """ Generates a key for the map based on the player's current location
            @ReturnType String """
        return '{}{}'.format(self._playerLocation[0], self._playerLocation[1])

    def getRooms(self):
        """ Returns the loaded map. It is slated for removal very soon and should
            not be used
            @ReturnType dict """
        return self.map

    def getDescriptionText(self):
        """ Gets the description text from the room at the player's current location

            @ReturnType String """
        text = self._visited[self._roomKey].getText()
        return text

    def getStatText(self):
        """ Returns a formatted string representation of the player's basic stats,
            including current health / max health, equipped weapon, and damage range """
        stats = "HP: {}/{}         Equipped weapon: {}        Damage: {}".format(
            self._player.getHP(), self._player.getMaxHP(),
            self._player._weapon._name, self._player._weapon.getDamage())
        return stats

    def _canMove(self, direction):
        """ Checks if there is a room in <direction> from current room """
        dirX, dirY = Controller.DIRECTIONS[direction]
        roomKey = '{}{}'.format(self._playerLocation[0] + dirX,
                                self._playerLocation[1] + dirY)
        return roomKey in self.map

    def getDirectionOptions(self):
        """ Builds the list of directions the player can move
            ReturnType list of Strings """
        return ["Move {}".format(x).title() for x in ["NORTH", "WEST", "EAST", "SOUTH"]
                if self._canMove(x)]

    def getActionOptions(self):
        """ Builds and returns the list of actions the player can take in the room
            ReturnType list of Strings """
        options = []
        # Try to add item to menu
        try:
            if not self._room.item.isHidden():
                logging.debug("Visible item in room")
                options.append("Pick up " + self._room.item.identify())
            else:
                logging.debug("Hidden item in room")
                options.append("Search room")
        except AttributeError:
            logging.debug("No item in room")
            pass
        # Try to add enemy to menu
        try:
            if not self._room.enemy.isDead():
                options.append("Fight " + self._room.enemy.getName())
        except AttributeError:
            pass
        # Try to add NPC to menu
        try:
            options.append("Interrogate " + self._room.character.getName())
        except AttributeError:
            pass

        return options

    def getGameOptions(self):
        """ Returns the metagame options (e.g. Save, Load, Quit)
            ReturnType list of strings """
        options = ["Save", "Load", "Exit game"]
        return options

    def movePlayer(self, direction):
        """ Updates the player's current location and instantiates a room if necessary
            ReturnType None """
        if not self._canMove(direction):
            return
        self._player.move(Controller.DIRECTIONS[direction])
        self._playerLocation = self._player.getLocation()
        self._roomKey = self.getRoomKey()
        try:
            logging.debug('Returning to previously visited room')
            self._room = self._visited[self._roomKey]
        except KeyError:
            logging.debug('Visiting a new room, generating room')
            self._visited[self._roomKey] = Factory.roomFactory(self._playerLocation[0],
                                                               self._playerLocation[1],
                                                               self.map[self._roomKey][1])
            self._room = self._visited[self._roomKey]
            logging.debug('Created new room')
        finally:
            logging.debug('Room %s', self._roomKey)
            logging.debug('Room description: %s', self._room.getText())

    def updateGameView(self):
        """ Updates the GameView screen after player action """

        self._gameView.updateDescription(self.getDescriptionText())
        self._gameView.updateStats(self.getStatText())
        self._gameView.updateDirectionMenu(self.getDirectionOptions())
        self._gameView.updateActionMenu(self.getActionOptions())
        self._gameView.setMenuFocus(0)

    def moveCallback(self, button):
        """ Updates the gameView object every time the player moves """
        functions = {'move_north': (self.movePlayer, "NORTH"),
                     'move_south': (self.movePlayer, "SOUTH"),
                     'move_east': (self.movePlayer, "EAST"),
                     'move_west': (self.movePlayer, "WEST")}
        label = button._w.original_widget.text.lower().replace(' ', '_')
        try:
            functions[label][0](functions[label][1])
        except KeyError:
            return
        self.updateGameView()

    def optionCallback(self, button):
        """ Updates the gameView object whenever the player uses the
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
        """ Updates the gameView object whenever the player performs an action from
            the action menu
            Precondition: Action menu item is selected by player. Action menu items should be in
                          the format 'pick up <item>', 'fight <enemy>', 'interrogate <npc>'
            Postcondition: The appropriate action method is run
            @ReturnType None"""
        label = button._w.original_widget.text.lower().replace(' ', '_')
        try:
            if self._room.item.isHidden():
                logging.debug("Trying to search the room")
                if self._room.search():
                    logging.debug("Found item %s", self._room.item.identify())
                    self._room.item.find()
                    self._room.updateText(
                        "You're in the hallway outside your office. \
This is where you found the {}.".format(self._room.item.identify()))
                else:
                    logging.debug("Item still hidden")
            else:
                logging.debug("Trying to add item to inventory")
                logging.debug(self._room.item)
                self._player.addItem(self._room.item)
                self._room.removeItem()
        except AttributeError:
            logging.debug("No item in room")
            try:
                logging.debug("Trying to fight enemy")
                self._player.fight(self._room.enemy)
                logging.debug("Fought enemy - results: Player HP: %s\nEnemy HP: %s",
                              self._player.getHP(),
                              self._room.enemy.getHP())
                if self._room.enemy.isDead():
                    self._room.killEnemy()
                else:
                    self.playerDead()
            except AttributeError:
                logging.debug("No enemy to fight")
                self._player.interrogate(self._room.character)
        finally:
            self.updateGameView()
            logging.debug("Action menu item %s pressed", label)

    def playerDead(self):
        """ Handle the player dying """
        pass

    def saveGame(self):
        """ Pickles the controller state and player to save the current game state
            Precondition: None
            Postcondition: Saves game state in saves/<player name>_<save index>
            @ReturnType None """
        try:
            makedirs(self._saveDir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        with open(self._saveDir+'/patrick_001', 'w+') as f:
            dill.dump(self._player, f)
            dill.dump(self._playerLocation, f)
            dill.dump(self._currentRoom, f)
            dill.dump(self.map, f)
            dill.dump(self._visited, f)
            dill.dump(self._roomKey, f)

    def loadGame(self):
        """ Unpickles the controller (self) and player (self._player) to load the
            saved game state
            Precondition: Save game file in saves/<player name>_<save index>
            Postcondition: Loads game state
            @ReturnType None """
        try:
            with open(self._saveDir+'/patrick_001') as f:
                self._player = dill.load(f)
                self._playerLocation = dill.load(f)
                self._currentRoom = dill.load(f)
                self.map = dill.load(f)
                self._visited = dill.load(f)
                self._roomKey = dill.load(f)
                self.updateGameView()
        except IOError:
            return
