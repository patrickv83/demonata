#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.character import Character
#from src.weapon import Weapon
import random
from enum import Enum

# Enumeration for Enemy Types
class EnemyType(Enum):
    BROWNIE = 1
    DROW = 2
    GOBLIN = 3
    THUG = 4
    DEMON = 5

# Enemy (superclass) creates an enemy
class Enemy(Character):
    def __init__(self, name, hp, dmg, enemyType):
        self.damage = dmg
        self.enemyType = enemyType
        super(Enemy, self).__init__(name, hp)

# Brownie is a pixie/flying creature with magic attacks. They have low hit points
# and low armor
class Brownie(Enemy):
    def __init__(self):
        super(Brownie, self).__init__(name="Brownie", hp=10, dmg=2, enemyType=BROWNIE)

# Drow is a dark elf with magic and bludgeoning attacks. They have low hit
# points and high armor
class Drow(Enemy):
    def __init__(self):
        super(Drow, self).__init__(name="Drow", hp=35, dmg=2, enemyType=DROW)

# Goblin has knife/sword attacks. The have medium hit points
# and low armor
class Goblin(Enemy):
    def __init__(self):
        super(Goblin, self).__init__(name="Goblin", hp=20, dmg=15, enemyType=GOBLIN)

# Thug has bludgeoning or knife/sword attacks. They have medium hit points
# and medium armor
class Thug(Enemy):
    def __init__(self):
        super(Thug, self).__init__(name="Thug", hp=25, dmg=15, enemyType=THUG)

# Demon is the boss enemy. Demons have magic and knife/sword attacks. They
# have a special life drain attack. Demons have high hit points and high armor
class Demon(Enemy):
    def __init__(self):
        super(Demon, self).__init__(name="Demon", hp=75, dmg=20, enemyType=DEMON)
        
