import pytest
from view import mainView

def test_main_view():
    descriptionText = 'main game text'
    mapText = 'map'
    choice1 = 'choice1'
    choice2 = 'choice2'
    choice3 = 'choice3'
    view = mainView.gameView(descriptionText, mapText, 
            [choice1, choice2, choice3])
    assert view.screen.body[0].get_text()[0] == descriptionText
    assert view.screen.body[1].get_text()[1] == mapText
    assert view.screen.footer.
