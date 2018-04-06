""" This is the main view for demonata, with a description field on top (with optional mini map)
and a dynamically generated player actions menu on the bottom """
import urwid
from view.button import ActionButton

# Topmost widget
# inner widget depth1 - description
# inner widget depth1 - menu

class GameView(object):
    """ The GameView class"""
    def __init__(self, descriptionText, mapText, menuChoices):
        self._walker = urwid.SimpleFocusListWalker([])
        self.mini_map = urwid.Pile([])
        menu = urwid.BoxAdapter(urwid.ListBox(self._walker), 6)
        self._map_text = mapText
        self._show_map()
        description = urwid.Filler(urwid.Text(descriptionText),
                                   valign='middle', height='pack')
        top = urwid.Overlay(self.mini_map, description, align='right',
                            height=('relative', 10), valign='top',
                            width=('relative', 10), min_width=20, min_height=10)
        self.screen = urwid.Frame(top, header=None, footer=menu, focus_part='footer')
        self._create_menu(menuChoices)

    def _show_map(self):
        self.mini_map = urwid.LineBox(urwid.Filler(urwid.Text(self._map_text), valign='middle',
                                                   height='pack'))

    def _hide_map(self):
        self.mini_map = urwid.Filler(urwid.Text(""), valign='middle',
                                     height='pack')

    def _toggle_map(self):
        if isinstance(self.mini_map, urwid.graphics.LineBox):
            self._hide_map()
        else:
            self._show_map()

    def _create_menu(self, choices):

        action_button_list = [ActionButton(choices[i], self._callback) for i in range(len(choices))]
        self._walker.append(urwid.Pile(action_button_list))

    def update_menu(self, choices=[]):
        self._walker = urwid.SimpleFocusListWalker([])
        self._create_menu(choices)

    def _callback(self):
        raise urwid.ExitMainLoop()

    def update_map(self, text):
        self._map_text = text
        if isinstance(self.mini_map, urwid.graphics.LineBox):
            self.mini_map._get_original_widget()._get_original_widget().set_text(text)


if __name__ == '__main__':
    view = GameView('Main game text', "Map",            # pylint: disable=I0011,C0103
                    ['Choice1', 'Choice2', 'Choice3'])
    urwid.MainLoop(view.screen, palette=[('reversed', 'standout', '')]).run()
