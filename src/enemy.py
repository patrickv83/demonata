""" Enemy Module
    Defines the Enemy superclass
    Defines each Enemy subclass
    Defines an enumerated list of Enemy Types (ET) """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.character import Character
#from src.weapon import Weapon
#import random
from enum import Enum

class ET(Enum):
    """ Enumerated list of Enemy Types (ET) """
    BROWNIE = 1
    DROW = 2
    GOBLIN = 3
    THUG = 4
    DEMON = 5
    DRAGON = 6

class Enemy(Character):
    """ Enemy superclass creates an enemy """
    def __init__(self, name, hp, dmg, enemyType):
        self.damage = dmg
        self.enemyType = enemyType
        super(Enemy, self).__init__(name, hp)

class Brownie(Enemy):
    """ Brownie is a pixie/flying creature with magic attacks.
        They have low hit points and low armor """
    def __init__(self):
        super(Brownie, self).__init__(name="Brownie", hp=10, dmg=2, enemyType=ET.BROWNIE)

class Drow(Enemy):
    """ Drow is a dark elf with magic and bludgeoning attacks.
        They have low hit points and high armor """
    def __init__(self):
        super(Drow, self).__init__(name="Drow", hp=35, dmg=2, enemyType=ET.DROW)

class Goblin(Enemy):
    """ Goblin has knife/sword attacks.
        They have medium hit points and low armor """
    def __init__(self):
        super(Goblin, self).__init__(name="Goblin", hp=20, dmg=15, enemyType=ET.GOBLIN)

class Thug(Enemy):
    """ Thug has bludgeoning or knife/sword attacks.
        They have medium hit points and medium armor """
    def __init__(self):
        super(Thug, self).__init__(name="Thug", hp=25, dmg=15, enemyType=ET.THUG)

class Demon(Enemy):
    """ Demon is the boss enemy
        Demons have magic and knife/sword attacks
        They have a special life drain attack
        Demons have high hit points and high armor """
    def __init__(self):
        super(Demon, self).__init__(name="Demon", hp=75, dmg=20, enemyType=ET.DEMON)
