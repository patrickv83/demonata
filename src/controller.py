from src.view.main_view import GameView
from src.view.initial_view import InitialView
from src.player import Player
from src.world import World

import urwid

class Controller(object):
    def __init__(self):

        self.player = Player("Patrick", 10, 15)
        self.world = World(self.player)

        self._game_view = GameView(self.world.getDescriptionText(), self.world.getMapText(),
                                   directions=self.world.getDirectionOptions(),
                                   actions=self.world.getActionOptions(),
                                   gameOpts=self.world.getGameOptions(),
                                   controller=self)

        self._initial_view = InitialView(['New game', 'Load game', 'Exit'], 
                                         self._game_view, game_loop=None)
        self._loop = urwid.MainLoop(self._initial_view.screen, 
                                    palette=[('reversed', 'standout', '')])
        self._initial_view.set_game_loop(self._loop)

    def start(self):
        self._loop.run()

    def stop(self):
        self._loop.stop()

