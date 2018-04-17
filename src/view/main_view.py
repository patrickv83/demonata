""" This is the main view for demonata, with a description field on top (with optional mini map)
and a dynamically generated player actions menu on the bottom """
import urwid

try:
    from view.button import ActionButton
except ImportError:
    from button import ActionButton

class GameView(object):
    """ The GameView class"""
    def __init__(self, description_text, map_text, directions, actions, gameOpts):
        # Room description stuff
        self.description = urwid.Filler(urwid.Text(description_text),
                                        valign='middle', height='pack')

        # Map stuff
        self._map_text = map_text
        self.mini_map = urwid.Pile([])
        if self._map_text: self.show_map()

        # Menu stuff
        direction_menu = urwid.Pile([ActionButton(direction, self._callback) for direction in directions])
        action_menu = urwid.Pile([ActionButton(action, self._callback) for action in actions])
        option_menu = urwid.Pile([ActionButton(opt, self._callback) for opt in gameOpts])
        self._walker = urwid.SimpleFocusListWalker([])
        cols = urwid.Columns([('weight', 20, direction_menu), 
                              ('weight', 40, action_menu), 
                              ('weight', 30, option_menu)], dividechars=2)
        self._walker.append(cols)
        self.menu = urwid.BoxAdapter(urwid.ListBox(self._walker), 6)



        top = urwid.Overlay(self.mini_map, self.description, align='right',
                            height=('relative', 10), valign='top',
                            width=('relative', 10), min_width=20, min_height=10)
        self.screen = urwid.Frame(top, header=None, footer=self.menu, focus_part='footer')

    def show_map(self):
        self.mini_map = urwid.LineBox(urwid.Filler(urwid.Text(self._map_text), valign='middle',
                                                   height='pack'))

    def hide_map(self):
        self.mini_map = urwid.Filler(urwid.Text(""), valign='middle',
                                     height='pack')

    def toggle_map(self):
        if isinstance(self.mini_map, urwid.graphics.LineBox):
            self.hide_map()
        else:
            self.show_map()

    def update_description(self, newText):
        self.description.base_widget.set_text(newText)


    def update_menu(self, choices):
        self._walker = urwid.SimpleFocusListWalker([])
        self._create_menu(choices)

    def _callback(self, button):
        raise urwid.ExitMainLoop()

    def update_map(self, text):
        self._map_text = text
        if isinstance(self.mini_map, urwid.graphics.LineBox):
            self.mini_map.original_widget.original_widget.set_text(text)


if __name__ == '__main__':
    view = GameView('Main game text', "Map",            # pylint: disable=I0011,C0103
                    ['Choice1', 'Choice2', 'Choice3'])
    urwid.MainLoop(view.build(), palette=[('reversed', 'standout', '')]).run()
