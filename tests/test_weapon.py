import pytest
from src.weapon import Weapon

def test_weapon_instance():
    wep = Weapon(5, "Test Weapon")
    assert wep.getDamage() == 5
    assert wep.getName() == "Test Weapon"
    assert wep.identify() == "Test Weapon"
    assert wep.appraise() == 5
    assert wep.describe() == "A weapon to be used in combat. Equip to increase your damage."

def test_create():
    wep = Weapon.create()
    assert 1 <= wep.getDamage() <= 5
    assert wep.appraise() == wep.getDamage() and 1 <= wep.appraise() <= 5
    assert wep.identify() != None
    assert wep.describe() == "A weapon to be used in combat. Equip to increase your damage."
