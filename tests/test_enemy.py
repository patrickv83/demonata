import unittest
from src.enemy import Enemy
#from src.weapon import Weapon

e = Brownie()
#d = Drow()
#g = Goblin()
#t = Thug()
#boss = Demon()
#f = Enemy("Generic", 25, 3, GOBLIN)

def test_enemy_instantiate():
    assert (e.getName() == "Brownie" and e.getHP() == 10)

def test_enemy_damage():
    e.takeDamage(5)
    assert e.getHP() == 5

def test_enemy_heal():
    e.heal(3)
    assert e.getHP() == 8

def test_enemy_name_change():
    e.setName("dead Brownie")
    assert e.getName() == "dead Brownie"

#def test_enemy_attack():
#    damage = e.attack(f)
#    assert f.getHP() == (25 - damage)

def test_enemy_dead():
    e.takeDamage(8)
    assert e.isDead() == True
