import unittest
import pytest
from src.npc import *

teacher = npc.Tutor()
bart = npc.Bartender()
nerd = npc.Bookworm()
granny = npc.Cashier()

def test_npc_instantiate():
    assert (teacher.getName() == "Tutor" and teacher.getHP() == 5)
    assert (bart.getName() == "Bartender" and bart.getHP() == 5)
    assert (nerd.getName() == "Bookworm" and nerd.getHP() == 5)
    assert (granny.getName() == "Cashier" and granny.getHP() == 5)

def test_npc_react():
    teacherReaction = teacher.react(2)
    assert teacherReaction == "This option doesn't get you an good info."

    bartReaction = bart.react(1)
    assert bartReaction == "I might have seen something."

    nerdReaction = nerd.react(3)
    assert nerdReaction == "Ok, I'm really not supposed to do this but the teaching assistant came in and purchased a copy of 'Advanced Demon Summoning.' Do you think he is really going to do it, summon a demon?"

    grannyReaction = granny.react(5)
    assert grannyReaction == "I don't understand, try again."

    grannyReaction = granny.react(1)
    assert grannyReaction == "He bought fifteen pounds of raw meat and some black candles. What an odd combination."
