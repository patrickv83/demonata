import pytest
from demonata.item import Item

def test_abstract_item_instantiate_fails():
    with pytest.raises(TypeError):
        Item()
