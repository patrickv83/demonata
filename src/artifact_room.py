#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.item_factory import ItemFactory
from src.room import Room

class ArtifactRoom(Room):
    def __init__(self, x, y, text, item=None):
        self.item = item or self.randomItem
        super(ArtifactRoom, self).__init__(x, y, text)

    def randomItem(self):
        return ItemFactory()

