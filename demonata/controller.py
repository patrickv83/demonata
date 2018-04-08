from view.main_view import GameView
from view.initial_view import InitialView
#from demonata.world import World
#from demonata.player import Player
import urwid

class Controller(object):
    _view = InitialView(['New game', 'Load game', 'Exit'])
    loop = urwid.MainLoop(_view.screen, palette=[('reversed', 'standout', '')])
    def __init__(self):
        #self.player = Player()
        self._view = Controller._view    
        self._loop = Controller.loop

    def start(self):
        self._loop.run()

    def stop(self):
        self._loop.stop()

    @classmethod
    def update_view(cls, view):
        views = {'new_game': GameView('Main game text', "Map", ['Choice1', 'Choice2', 'Choice3'])}
        if view in views:
            cls.loop.widget = views[view].build()
            cls.loop.draw_screen()

