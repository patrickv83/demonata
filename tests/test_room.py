import pytest
from demonata.item import Room

def abstract_room_instantiate_fails():
  with pytest.raises(TypeError):
    Room()

