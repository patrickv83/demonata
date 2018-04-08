"""Custom urwid.Button implementation"""
import urwid

class ActionButton(urwid.Button):
    """Custom urwid.Button implementation with default callback and method to add new callback"""
    def __init__(self, caption, callback):
        super(ActionButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback)
        self._w = urwid.AttrMap(urwid.SelectableIcon(caption, len(caption)+1),
                                None, focus_map='reversed')

    def update_callback(self, callback, args):
        urwid.connect_signal(self, 'click', callback, user_args=args)
