from src.view.main_view import GameView
from src.view.initial_view import InitialView
from src.world import World
#from src.player import Player
import urwid

class Controller(object):
    def __init__(self):
        #self.player = Player()
        self.world = World()
        self._game_view = GameView(self.world.getDescriptionText(), self.world.getMapText(), 
                                   self.world.getMenuOptions())
        self._initial_view = InitialView(['New game', 'Load game', 'Exit'], 
                                         self._game_view, game_loop=None)
        self._loop = urwid.MainLoop(self._initial_view.screen, 
                                    palette=[('reversed', 'standout', '')])
        self._initial_view.set_game_loop(self._loop)

    def start(self):
        self._loop.run()

    def stop(self):
        self._loop.stop()

