from random import choice

from item import Item
#from consumable import Consumable
from weapon import Weapon

class ItemFactory(object):
    # Create Item
    @staticmethod
    def create():
        itemTypes = Item.__subclasses__()

        return itemTypes[choice(itemTypes)]()
