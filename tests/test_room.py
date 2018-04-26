import pytest
from src.room import Room
from src.artifact_room import ArtifactRoom
from src.enemy_room import EnemyRoom
from src.factory import Factory

def test_empty_room_class_and_methods():
    er = Room(1, 1, ["Description"])
    x, y = er.getCoords()
    desc = er.getText()
    assert (x == 1 and y == 1 and desc == "Description")

def test_artifact_room_class_and_methods():
    item = Factory.itemFactory()
    ar = ArtifactRoom(2, 2, ["text"], item=item)
    x, y = ar.getCoords()
    desc = ar.getText()
    assert (x == 2 and y == 2 and desc == "text" and item == ar.getItem())
