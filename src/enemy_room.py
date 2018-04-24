#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.room import Room
from src.factory import Factory

class EnemyRoom(Room):
    """ EnemyRoom class """
    def __init__(self, x, y, text, enemy=None):
        self.enemy = enemy or self.randomEnemy()
        super(EnemyRoom, self).__init__(x, y, text)

    def modifyPlayer(self, player):
        """ Update player with results of enemy interaction """
        return player


    def randomEnemy(self):
        """ Precondition: None
            Postcondition: returns random Enemy """
        return Factory.enemyFactory()
