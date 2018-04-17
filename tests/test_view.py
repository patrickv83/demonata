import pytest
from src.view.main_view import GameView

class gvTest():
    def __init__(self):
        self.description_text = 'main game text'
        self.map_text = 'map'
        self.dir1 = 'Move north'
        self.dir2 = 'Move south'
        self.action1 = 'Fight the chicken'
        self.action2 = 'Pick up chicken nugget'
        self.option1 = 'Save game'
        self.option2 = 'Load game'
        self.option3 = 'Exit game'
        self.view = GameView(self.description_text, self.map_text, 
                             directions=[self.dir1, self.dir2],
                             actions=[self.action1, self.action2],
                             gameOpts=[self.option1, self.option2, self.option3])

def test_main_view():
    test = gvTest()
    assert test.view.screen.body[0].get_text()[0] == test.description_text
    assert test.view.screen.body[1].get_text()[0] == test.map_text
    # Move menu
    assert test.view.screen.footer.original_widget.body[0][0][0]._w.original_widget.text == test.dir1
    assert test.view.screen.footer.original_widget.body[0][0][1]._w.original_widget.text == test.dir2

    # Action menu
    assert test.view.screen.footer.original_widget.body[0][1][0]._w.original_widget.text == test.action1
    assert test.view.screen.footer.original_widget.body[0][1][1]._w.original_widget.text == test.action2

    # Option menu
    assert test.view.screen.footer.original_widget.body[0][2][0]._w.original_widget.text == test.option1
    assert test.view.screen.footer.original_widget.body[0][2][1]._w.original_widget.text == test.option2
    assert test.view.screen.footer.original_widget.body[0][2][2]._w.original_widget.text == test.option3
