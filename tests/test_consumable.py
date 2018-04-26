import unittest
from src.consumable import Consumable

c = Consumable("test name", 5, 5)

def test_consumable_instantiate():
    assert c.getName() == "test name" and c.appraise() == 5 and c.getUses() == 5

def test_consumable_consume():
    c.consume()
    assert c.getUses() == 4
    c.consume()
    assert c.getUses() == 3
    c.consume()
    assert c.getUses() == 2
    c.consume()
    assert c.getUses() == 1
    c.consume()
    assert c.getUses() == 0

def test_consumable_change():
    c.setName("half-eaten bread")
    assert c.getName() == "half-eaten bread"

def test_consumable_value_change_on_consume():
    c.consume()
    assert c.getValue() == 0
    c2 = Consumable("test name2", 10, 5)
    assert c2.getValue() == 10
    c2.consume()
    assert c2.getValue() == 10
    c2.consume()
    assert c2.getValue() == 10
    c2.consume()
    assert c2.getValue() == 10
    c2.consume()
    assert c2.getValue() == 10
    c2.consume()
    assert c2.getValue() == 0
    c2.consume()
    assert c2.getValue() == 0

def test_create():
    c = Consumable.create()
    assert 1 <= c.getUses() <= 3
    assert 1 <= c.appraise() <= 10
    assert c.identify() != None
    assert c.describe() != None