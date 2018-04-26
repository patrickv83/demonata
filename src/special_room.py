""" Bar Module
    Special Room """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.room import Room
from src.npc import NPC

class Bar(Room):
    # Bar - Special Room
    def __init__(self, x, y):
        self.bartender = NPC(name = "Bartender", hp = 5)
        super(Bar, self).__init__(self, x, y)

    def introText(self):
        return

    def modifyPlayer(self, player):
        #Update player with results 
