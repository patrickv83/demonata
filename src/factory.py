""" The factory module, with various types of factories """
from random import choice
import logging

class Factory(object):
    """ The Factory class, which holds the various factories as class methods """

    @staticmethod
    def enemyFactory():
        """ The enemy factory method, which returns a random enemy
            Precondition: None
            Postcondition: Returns a randomly selected Enemy type"""

        from src.enemy import *
        enemyTypes = Enemy.__subclasses__()
        pick = choice(enemyTypes)()
        logging.debug("Creating new enemy of type {}".format(pick))
        return pick

    @staticmethod
    def itemFactory():
        """ The item factory method, for generating random Items 
            Precondition: None
            Postcondition: Returns an instance of the randomly selected Item type """

        from src.item import Item
        #from consumable import Consumable # pylint: disable=unused-import
        from src.weapon import Weapon # pylint: disable=unused-import
        itemTypes = Item.__subclasses__()
        pick = itemTypes[choice(itemTypes)]()
        logging.debug("Creating new item of type {}".format(pick))
        return pick

    @staticmethod
    def roomFactory(x, y, text):
        """ The room factory method, for generating random Rooms
            Precondition: x, y coordinates (int), room description text (string)
            Postcondition: Returns an instance of the randomly selected Room type"""

        from src.room import Room
        from src.artifact_room import ArtifactRoom # pylint: disable=unused-import
        from src.enemy_room import EnemyRoom # pylint: disable=unused-import

        roomTypes = Room.__subclasses__()
        roomTypes.append(Room)
        pick = choice(roomTypes)(x, y, text)
        logging.debug("Creating new room of type {} at location ({}, {})".format(pick, x, y))
        return pick
