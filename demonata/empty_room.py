#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Room import Room

class EmptyRoom(Room):
    def introText(self):
        """@ReturnType void"""
        pass

    def __init__(self, x, y):
        self.___x = x
        self.___y = y

