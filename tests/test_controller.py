import pytest
from random import choice

from src.controller import Controller
from src.player import Player

controller = Controller()

def test_controller_import_map():
    assert len(controller.getRooms()) == 77

def test_new_game_player_at_origin():
    assert controller.getPlayerLocation() == (0, 0)

def test_can_only_move_north_from_origin():
    assert controller.getDirectionOptions() == ["Move North"]

def test_default_action_options():
    defaultActionOpts = []
    assert controller.getActionOptions() == defaultActionOpts

def test_default_game_options():
    defaultGameOpts = ["Save", "Load", "Exit game"]
    assert controller.getGameOptions() == defaultGameOpts

def test_move_player_north():
    controller.movePlayer("NORTH")
    assert controller.getPlayerLocation() == (0, 1)

def test_player_can_move_north_or_south():
    assert controller.getDirectionOptions() == ["Move North", "Move South"]

def test_description_correct_after_20_moves():
    for _ in range(20):
        controller.movePlayer(choice(Controller.DIRECTIONS.keys()))
    assert controller.getDescriptionText() == controller.map[controller._roomKey][1][0]

