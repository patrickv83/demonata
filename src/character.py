""" Character Module
    Serves as a superclass to Player and Enemy classes """
import random

class Character(object):
    """ Character type """
    def __init__(self, name, hp):
        """@ReturnType Character"""
        self._name = name        # @AttributeType String
        self._hp = hp            # @AttributeType int

    def getName(self):
        """@ReturnType String"""
        return self._name

    def setName(self, name):
        """@ReturnType Void - sets character name"""
        self._name = name

    def getHP(self):
        """@ReturnType int"""
        return self._hp

    def setHP(self, hp):
        """Sets character hp"""
        self._hp = hp

    def heal(self, hp):
        """Increases character hp"""
        self.setHP(self._hp + hp)

    def takeDamage(self, hp):
        """Decreases character hp"""
        self.setHP(self._hp - hp)

    def isDead(self):
        """@ReturnType boolean"""
        return self._hp <= 0

    #def attack(self, target):
     #   """@ReturnType int"""
     #   try:
     #       weaponDamage = self._weapon.getDamage()
     #   except AttributeError:
     #       weaponDamage = 0
     #   damage = random.randint(1, 1 + self._baseDamage + weaponDamage)
     #   target.takeDamage(damage)
     #   return damage
