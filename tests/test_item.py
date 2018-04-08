import pytest
from demonata.Item import Item

def test_abstract_item_instantiate_fails():
    with pytest.raises(TypeError):
        Item()
