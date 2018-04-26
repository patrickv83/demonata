import pytest
from src.room import Room

def test_empty_room_class_and_methods():
    er = Room(1, 1, ["Description"])
    x, y = er.getCoords()
    desc = er.getText()
    assert (x == 1 and y == 1 and desc == "Description")
