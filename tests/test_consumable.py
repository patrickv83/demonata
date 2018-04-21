import unittest
from src.consumable import *

consumableType = CT.BREAD
e = Bread()

def test_consumable_instantiate():
    assert (e.getName() == "Bread" and e.getUses() == 2 and e.getValue() == 5)

def test_consumable_consume():
    e.consume()
    assert e.getUses() == 1

def test_enemy_heal():
    e.heal(3)
    assert e.getHP() == 8

def test_consumable_change():
    e.setName("half-eaten bread")
    assert e.getName() == "half-eaten breads"

def test_consumable_empty():
    e.consume()
    assert e.getValue() == 0
