import unittest
from demonata.Player import Player
from demonata.Enemy import Enemy
from demonata.Weapon import Weapon

e = Enemy("mean joe", 15)
p = Player("sword gumby", 25, 3, weapon = Weapon("sword", "neat shiny sword", 3, 5))

def test_player_instantiate():
    assert (p.getName() == "sword gumby" and p.getHP() == 25 and p.getWeapon() == None)

def test_player_damage():
    p.takeDamage(5)
    assert p.getHP() == 20

def test_player_heal():
    p.heal(3)
    assert p.getHP() == 23

def test_player_name_change():
    newName = "angry sword gumby"
    p.setName(newName)
    assert p.getName() == newName

def test_player_attack():
    damage = p.attack(e)
    assert e.getHP() == (15 - damage)

def test_player_dead():
    p.takeDamage(23)
    assert p.isDead() == True
