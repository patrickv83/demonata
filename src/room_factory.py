""" The room factory module, for generating random Rooms """
from random import choice

from src.room import Room
from src.artifact_room import ArtifactRoom # pylint: disable=unused-import
from src.enemy_room import EnemyRoom # pylint: disable=unused-import

def roomFactory(x, y, text):
    """ Precondition: x, y coordinates (int), room description text (string)
        Postcondition: Returns an instance of the randomly selected Room type"""
    roomTypes = Room.__subclasses__()
    roomTypes.append(Room)
    return roomTypes[choice(roomTypes)](x, y, text)
