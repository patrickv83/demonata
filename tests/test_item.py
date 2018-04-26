import pytest
from src.item import Item

def test_item_functions():
    name = "A shiny bauble"
    desc = "A tiny golden bauble, not good for much but very shiny"
    value=5
    item = Item(name=name, desc=desc, value=value)

    assert item.identify() == name
    assert item.describe() == desc
    assert item.appraise() == value
