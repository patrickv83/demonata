#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item import Item
from src.room import Room

class ArtifactRoom(Room):
    def __init__(self, x, y, item):
        """@ReturnType Artifact Room"""
        self.___item = item
        """@AttributeType Item"""
        super(ArtifactRoom, self).__init__(x, y)

    def addArtifact(self):
        """@ReturnType void"""
        pass

    def modifyPlayer(self, player):
        pass

