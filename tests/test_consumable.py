import unittest
from src.consumable import *

consumableType = CT.BREAD
c = Bread()

def test_consumable_instantiate():
    assert (c.getName() == "Bread" and c.getUses() == 2 and c.getValue() == 5)

def test_consumable_consume():
    c.consume()
    assert c.getUses() == 1

def test_consumable_change():
    c.setName("half-eaten bread")
    assert c.getName() == "half-eaten bread"

def test_consumable_empty():
    c.consume()
    assert c.getValue() == 0
