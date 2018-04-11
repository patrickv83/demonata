#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.room import Room

class EmptyRoom(Room):
    def introText(self):
        """@ReturnType void"""
        pass

    def __init__(self, x, y, text):
        self.description = text
        super(EmptyRoom, self).__init__(x, y)

    def getCoordinates(self):
        return self.x, self.y
