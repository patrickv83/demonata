#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item import Item
import random

class Weapon(Item):
    def __init__(self, damage, name, desc = " ", value = 0):
        """@ReturnType Weapon"""
        self.__damage = damage
        """@AttributeType int"""
        self.__name = name
        """@AttributeType String"""
        self.__value = value
        """@AttributeType int"""
        self.__desc = desc
        """@AttributeTupe String"""
        super(Weapon, self).__init__(name, desc, value)

    def getDamage(self):
        return self.__damage

    def getName(self):
        return self.__name

    def __str__(self):
        """@ReturnType String"""
        return "Name: {0}\nDamage: {1}\nValue: {2}".format(self.__name, self.__damage, self.__value)

    @classmethod
    def getWeapon(cls):
        """@ReturnType Weapon"""
        weaponDamage = random.randint(1,5)
        weaponName = Weapon.__generateWeaponName()
        weaponValue = weaponDamage
        return cls(weaponDamage, weaponName, " ", weaponValue)

    def __generateWeaponName(self):
        """@ReturnType String"""
        return Weapon.__getAdjective() + Weapon.__getNoun()

    def __getAdjective(self):
        """@ReturnType String"""
        adjectives = ["Strong", "Weak", "Heavy", "Light", "Sharp", "Dull", "Blinding", "Cold", "Ice", "Fire",
                               "Earth", "Wind", "Freezing", "Burning", "Frightening", "Scary", "Beautiful", "Splendid",
                               "Atomic", "Basic", "Deadly", "Destructive", "Fatal", "Lethal", "Common", "Rare", "Epic",
                               "Legendary", "Devastating", "Effective", "Great", "Awesome", "Indestructable", "New",
                               "Invincible", "Ordinary", "Reliable", "Unreliable", "Sacred", "Simple", "Blessed",
                               "Cursed", "Magical", "Superior", "Useless", "Usefull", "Valuable", "Invaluable", "Used",
                               "Worthless", "Worthy", "Dreadful", "Enchanted", "Murderous", "Venomous", "Reliable",
                               "Poisonous", "Ultimate", "Unique", "Savage", "Dreadful", "Powerful", "Broken",
                               "Heavily Used", "Gently Used", "Pristine"]
        # 66 Total Adjectives
        return random.choice(adjectives)

    def __getNoun(self):
        """@ReturnType String"""
        nouns = ["Sword", "Axe", "Knife", "Dagger", "Diabo", "Pickaxe", "Shiv", "Sickle", "Mattock",
                          "Broadsword", "Katana", "Longsword", "Sabre", "Ulfberht", "Battle Axe", "Flail", "Mace",
                          "Morning Star", "Spear", "Halberd", "Lance", "Bardiche", "Glaive", "Tomahawk", "Pike",
                          "Scythe", "Bow", "Sling", "Long Bow", "Compound Bow", "Recurve Bow", "Throwing Axe",
                          "Mongol Bow", "Crossbow", "Javelin", "Wand", "Staff", "Quarterstaff", "Club", "Bat", "Diabo",
                          "Hammer", "Sledgehammer", "Maul", "Crowbar"]
        # 45 Total Nouns
        return random.choice(nouns)

