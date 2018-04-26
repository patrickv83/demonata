""" Consumable Module
    A consumable is tem with a name, value, a limited number of uses, and a generic description.
    A consumable is used to restore HP. """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from src.item import Item

class Consumable(Item):
    """ Consumable, creates a consumable item with a name, value, a limited number of uses, and a
     generic description."""
    def __init__(self, name, value, uses,
                 desc="A consumable item. Use this item to restore heal. \
                 Consumables have a limited number of uses."):
        """@ReturnType Consumable"""
        self._uses = uses
        """@AttributeType int"""
#        self.consumableType = consumableType
        super(Consumable, self).__init__(name, desc, value)

    def getUses(self):
        """ Get the number of times the consumable can be used. """
        return self._uses

    def getName(self):
        """ Get the name of the consumable. """
        return self._name

    def consume(self):
        """ When the consumable is consumed, this method must be called.
        This will decrease the number of uses the consumable has. """
        if self._uses == 0:
            self._value = 0
            return
        self._uses -= 1

    def getValue(self):
        """ Get the value of the consumable.  If the consumable has
        no uses left, this will return 0. """
        if self._uses == 0:
            return 0
        return self._value

    def __str__(self):
        """@ReturnType String"""
        return "Name: {0}\nUses: {1}\nValue: {2}".format(self._name, self._uses, self._value)

    @classmethod
    def create(cls):
        """Generate a random consumable with random name, value, and uses.
        @ReturnType: Consumable"""
        consumableName = Consumable._generateConsumableName()
        consumableValue = random.randint(1, 10)
        consumableUses = random.randint(1, 3)
        return cls(consumableName, consumableValue, consumableUses)

    @staticmethod
    def _generateConsumableName():
        """Generate a random consumable name consisting of an adjective followed by a noun.
        @ReturnType: String"""
        adjective = Consumable._getAdjective()
        noun = Consumable._getNoun()
        return adjective + " " + noun

    @staticmethod
    def _getAdjective():
        """Private helper function to get a random adjective for consumables
        @ReturnType: String"""
        adjectives = ["Moldy", "Rotten", "Stinky", "Smelly", "Golden", "Silver", "Bronze",
                      "Healthy", "Delicious", "Tasty", "Frozen", "Organic", "Half Eaten", "Bitten",
                      "Chewed On", "Large", "Small", "Over-sized", "Tiny", "Ripe", "Over-ripe"]
        return random.choice(adjectives)

    @staticmethod
    def _getNoun():
        """Private helper funcrtion to get a random noun for consumables
        @ReturnType: String"""
        nouns = ["Nuts", "Peanuts", "Almonds", "Walnuts", "Cashews", "Brazil Nuts", "Apple",
                 "Honey Crisp Apple", "Apricot", "Banana", "Grapes", "Peach", "Plums", "Beet",
                 "Carrot", "Celery", "Squash", "Zucchini", "Avocado", "Corn Cob", "Onion", "Potato",
                 "Sweet Potato", "Yam"]
        return random.choice(nouns)
