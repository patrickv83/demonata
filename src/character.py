""" Character Module
    Serves as a superclass to Player and Enemy classes """
import random

class Character(object):
    """ Character type """
    def __init__(self, name, hp):
        """@ReturnType Character"""
        self.___name = name        # @AttributeType String
        self.___hp = hp            # @AttributeType int

    def getName(self):
        """@ReturnType String"""
        return self.___name

    def setName(self, name):
        """@ReturnType Void - sets character name"""
        self.___name = name

    def getHP(self):
        """@ReturnType int"""
        return self.___hp

    def setHP(self, hp):
        """Sets character hp"""
        self.___hp = hp

    def heal(self, hp):
        """Increases character hp"""
        self.setHP(self.___hp + hp)

    def takeDamage(self, hp):
        """Decreases character hp"""
        self.setHP(self.___hp - hp)

    def isDead(self):
        """@ReturnType boolean"""
        return self.___hp <= 0

    #def attack(self, target):
     #   """@ReturnType int"""
     #   try:
     #       weaponDamage = self.___weapon.getDamage()
     #   except AttributeError:
     #       weaponDamage = 0
     #   damage = random.randint(1, 1 + self.___baseDamage + weaponDamage)
     #   target.takeDamage(damage)
     #   return damage
