""" This is the initial view for demonata, with a menu for starting a new game or
resuming a saved game """
import urwid

from src.view.button import ActionButton

class InitialView(object):
    """ The InitialView class"""
    def __init__(self, menu_choices, game_view, game_loop=None, controller=None):
        self._walker = urwid.SimpleFocusListWalker([])
        self.screen = urwid.ListBox(self._walker)
        self._create_menu(menu_choices)
        self._game_loop = game_loop
        self._game_view = game_view
        self._controller = controller

    def set_game_loop(self, loop):
        self._game_loop = loop

    def _create_menu(self, choices):
        action_button_list = [ActionButton(choices[i], self._callback) for i in range(len(choices))]
        self._walker.append(urwid.Pile(action_button_list))

    def _exit(self):
        raise urwid.ExitMainLoop()

    def _new_game(self):
        self._game_loop.widget = self._game_view.screen

    def _load_game(self):
        self._game_loop.widget = self._game_view.screen
        self._controller.loadGame()

    def _callback(self, button):
        functions = {'new_game': self._new_game, 'load_game': self._load_game, 'exit': self._exit}
        label = button._w.original_widget.text.lower().replace(' ', '_')
        if label in functions:
            functions[label]()

