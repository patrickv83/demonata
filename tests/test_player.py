import unittest
from src.player import Player
from src.enemy import *
from src.weapon import Weapon
from src.consumable import *

e = Enemy("Brownie", 10, 2, ET.BROWNIE)
p = Player("sword gumby", 25, weapon = Weapon(name="sword", damage=5))
bread = Bread();

def test_player_instantiate():
    assert (p.getName() == "sword gumby" and p.getHP() == 25)

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

#def test_player_attack():
#    damage = p.attack(e)
#    assert e.getHP() == (15 - damage)
def test_player_consumable_heals():
    p.consume(bread)
    assert p.getHP() == 23+bread.getValue()

def test_player_dead():
    p.takeDamage(28)
    assert p.isDead() == True
    
def test_dead_cannot_eat():
    assert p.isDead()
    p.consume(bread)
    assert p.isDead()
    

