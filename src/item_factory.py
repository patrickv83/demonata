""" The item factory module, for generating random Items """
from random import choice

from src.item import Item
#from consumable import Consumable # pylint: disable=unused-import
from src.weapon import Weapon # pylint: disable=unused-import

def itemFactory():
    """ Precondition: None
        Postcondition: Returns an instance of the randomly selected Item type"""
    itemTypes = Item.__subclasses__()

    return itemTypes[choice(itemTypes)]()
