import unittest
from demonata.enemy import Enemy
from demonata.weapon import Weapon

e = Enemy("mean joe", 15)
f = Enemy("sword gumby", 25, 3, weapon = Weapon("sword", "neat shiny sword", 3, 5))

def test_enemy_instantiate():
    assert (e.getName() == "mean joe" and e.getHP() == 15 and e.getWeapon().getName() == 'Cudgel')

def test_enemy_damage():
    e.takeDamage(5)
    assert e.getHP() == 10

def test_enemy_heal():
    e.heal(3)
    assert e.getHP() == 13

def test_enemy_name_change():
    e.setName("dead mean joe")
    assert e.getName() == "dead mean joe"

def test_enemy_attack():
    damage = e.attack(f)
    assert f.getHP() == (25 - damage)

def test_enemy_dead():
    e.takeDamage(13)
    assert e.isDead() == True
