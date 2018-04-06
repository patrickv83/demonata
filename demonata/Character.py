#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Item

class Character(object):
    def __init__(self, name, hp):
        """@ReturnType Character"""
        self.___name = name
        """@AttributeType String"""
        self.___hp = hp
        """@AttributeType Int"""
        self.___inventory = list()
        # @AssociationType Item

    def isDead(self):
        """@ReturnType boolean"""
        pass

