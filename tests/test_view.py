import pytest
from view.main_view import GameView

def test_main_view():
    description_text = 'main game text'
    map_text = 'map'
    choice1 = 'choice1'
    choice2 = 'choice2'
    choice3 = 'choice3'
    view = gameView(description_text, map_text, 
            [choice1, choice2, choice3])
    assert view.build().body[0].get_text()[0] == description_text
    assert view.build().body[1].get_text()[1] == map_text
    assert view.build().footer.original_widget.body[0][0]._w.original_widget.text == choice1
    assert view.build().footer.original_widget.body[0][1]._w.original_widget.text == choice2
    assert view.build().footer.original_widget.body[0][2]._w.original_widget.text == choice3
