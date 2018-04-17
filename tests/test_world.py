import pytest
from src.world import World
from src.player import Player

player = Player("Test guy", 15, 10)
world = World(player)

def test_world_import_map():
    assert len(world.getRooms()) == 77

def test_new_game_player_at_origin():
    assert world.getPlayerLocation() == (0, 0)

def test_can_only_move_north_from_origin():
    assert world.getDirectionOptions() == ["Move North"]

def test_default_action_options():
    defaultActionOpts = ["Fight pixie", "Pick up whatsit", "Interrogate djinn"]
    assert world.getActionOptions() == defaultActionOpts

def test_default_game_options():
    defaultGameOpts = ["Save", "Load", "Exit game"]
    assert world.getGameOptions() == defaultGameOpts

def test_move_player_north():
    world.movePlayer(World.NORTH)
    assert world.getPlayerLocation() == (0, 1)

def test_player_can_move_north_or_south():
    assert world.getDirectionOptions() == ["Move North", "Move South"]
