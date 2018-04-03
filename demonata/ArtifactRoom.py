#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Item import Item
from Room import Room

class ArtifactRoom(Room):
    def __init__(self, x, y, item):
        """@ReturnType Artifact Room"""
        self.___item = item
        """@AttributeType Item"""
        self._unnamed_World_ = None
        # @AssociationType World
        super(ArtifactRoom, self).__init__(x, y)

    def addArtifact(self, player):
        """@ReturnType void"""
        pass

    def modifyPlayer(self, player):
        pass

