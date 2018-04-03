#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Room import Room

class EmptyRoom(Room):
    def introText(self):
        """@ReturnType void"""
        pass

    def modifyPlayer(self, player):
        """@ReturnType void"""
        pass

    def operation(self):
        pass

    def __init__(self):
        self.___World_ = None
        # @AssociationType World

