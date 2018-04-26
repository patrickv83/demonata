#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Weapon class for generating weapons."""
import random
from src.item import Item

class Weapon(Item):
    """Weapon class for generating weapons."""
    def __init__(self, damage=5, name=None):
        """Weapon constructor, initializes damage, name, description, and value.
         ReturnType Weapon"""
        self._damage = damage
        """@AttributeType int"""
        super(Weapon, self).__init__(name or Weapon._generateWeaponName(),
                                     "A weapon to be used in combat. \
                                     Equip to increase your damage.",
                                     damage)

    def getDamage(self):
        """@ReturnType int"""
        return self._damage

    def getName(self):
        """ReturnType String"""
        return self.identify()

    def __str__(self):
        """ReturnType String"""
        return "Name: {0}\nDamage: {1}\nValue: {2}".format(self._name, self._damage, self._damage)

    @classmethod
    def create(cls):
        """Returns a randomly generated weapon with random values for name, damage, and value.
        ReturnType Weapon"""
        weaponDamage = random.randint(1, 5)
        weaponName = Weapon._generateWeaponName()
        return cls(weaponDamage, weaponName)

    @staticmethod
    def _generateWeaponName():
        """Generates a random weapon name. Private helper function.
        ReturnType String"""
        return Weapon._getAdjective() + " " + Weapon._getNoun()

    @staticmethod
    def _getAdjective():
        """Private helper function for getting a random adjective.
        ReturnType String"""
        adjectives = ["Strong", "Weak", "Heavy", "Light", "Sharp", "Dull", "Blinding", "Cold",
                      "Ice", "Fire", "Earth", "Wind", "Freezing", "Burning", "Frightening", "Scary",
                      "Beautiful", "Splendid", "Atomic", "Basic", "Deadly", "Destructive", "Fatal",
                      "Lethal", "Common", "Rare", "Epic", "Legendary", "Devastating", "Effective",
                      "Great", "Awesome", "Indestructable", "New", "Invincible", "Ordinary",
                      "Reliable", "Unreliable", "Sacred", "Simple", "Blessed", "Cursed", "Magical",
                      "Superior", "Useless", "Usefull", "Valuable", "Invaluable", "Used",
                      "Worthless", "Worthy", "Dreadful", "Enchanted", "Murderous", "Venomous",
                      "Reliable", "Poisonous", "Ultimate", "Unique", "Savage", "Dreadful",
                      "Powerful", "Broken", "Heavily Used", "Gently Used", "Pristine", "Golden",
                      "Silver", "Bronze", "Iron"]
        # 70 Total Adjectives
        return random.choice(adjectives)

    @staticmethod
    def _getNoun():
        """Private helper function for getting a random noun.
        ReturnType String"""
        nouns = ["Sword", "Axe", "Knife", "Dagger", "Diabo", "Pickaxe", "Shiv", "Sickle", "Mattock",
                 "Broadsword", "Katana", "Longsword", "Sabre", "Ulfberht", "Battle Axe", "Flail",
                 "Mace", "Morning Star", "Spear", "Halberd", "Lance", "Bardiche", "Glaive",
                 "Tomahawk", "Pike", "Scythe", "Bow", "Sling", "Long Bow", "Compound Bow",
                 "Recurve Bow", "Throwing Axe", "Mongol Bow", "Crossbow", "Javelin", "Wand",
                 "Staff", "Quarterstaff", "Club", "Bat", "Diabo", "Hammer", "Sledgehammer", "Maul",
                 "Crowbar"]
        # 45 Total Nouns
        return random.choice(nouns)
