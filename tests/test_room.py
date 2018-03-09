import pytest
from demonata.room import Room

def abstract_room_instantiate_fails():
  with pytest.raises(TypeError):
    Room()

