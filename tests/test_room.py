import pytest
from src.room import Room
from src.empty_room import EmptyRoom

def test_abstract_room_instantiate_fails():
    with pytest.raises(TypeError):
        Room(1, 1, "")


def test_empty_room_class_and_methods():
    er = EmptyRoom(1, 1, "")
    x, y = er.getCoordinates()
    er.introText()
    desc = er.description
    assert (x == 1 and y == 1 and desc == "")
