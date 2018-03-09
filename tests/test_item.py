import pytest
from demonata.item import Item

def test_item_instantiate_fails():
  with pytest.raises(TypeError):
    Item()
