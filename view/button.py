"""Custom urwid.Button implementation with custom cursor-hiding label class"""
import urwid

class Buttonlabel(urwid.SelectableIcon):
    """Custom SelectableIcon implementation to hide cursor in menus"""
    def __init__(self, text):
        curs_pos = len(text) + 1
        urwid.SelectableIcon.__init__(self, text, cursor_position=curs_pos)

class ActionButton(urwid.Button):
    """Custom urwid.Button implementation with default callback and method to add new callback"""
    def __init__(self, caption, callback):
        super(ActionButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback)
        self._w = urwid.AttrMap(Buttonlabel(caption),
                                None, focus_map='reversed')
