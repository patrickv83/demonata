""" This is the main view for demonata, with a description field on top (with optional mini map)
and a dynamically generated player actions menu on the bottom """
import urwid

from src.view.button import ActionButton

class GameView(object):
    """ The GameView class"""
    def __init__(self, descriptionText, statText, **kwargs):
        # Room description widget
        self.description = urwid.Filler(urwid.Text(descriptionText),
                                        valign='middle', height='pack')

        # Stat display widget
        self._statText = urwid.Text(statText)

        # kwargs
        directions = kwargs['directions']
        actions = kwargs.pop('actions', None)
        gameOpts = kwargs.pop('gameOpts', None)
        self._controller = kwargs.pop('controller', None)

        # Menu stuff
        optionMenu = urwid.Pile([ActionButton(opt, self._controller.optionCallback)
                                 for opt in gameOpts])
        self.walker = urwid.SimpleFocusListWalker([])
        cols = urwid.Columns([('weight', 20, self.createDirectionMenu(directions)),
                              ('weight', 40, self.createActionMenu(actions)),
                              ('weight', 30, optionMenu)], dividechars=2)
        self.walker.append(cols)
        self.menu = urwid.BoxAdapter(urwid.ListBox(self.walker), 6)

        self.screen = urwid.Frame(self.description, header=self._statText, 
                                  footer=self.menu, focus_part='footer')

    def setMenuFocus(self, column):
        self.walker[0].set_focus_column(column)

    def updateDescription(self, newText):
        self.description.base_widget.set_text(newText)

    def createDirectionMenu(self, directions):
        return urwid.Pile([ActionButton(direction, self._controller.moveCallback)
                           for direction in directions])

    def createActionMenu(self, actions):
        return urwid.Pile([ActionButton(action, self._controller.actionCallback)
                           for action in actions])

    def updateDirectionMenu(self, options):
        self.walker[0].contents[0] = (self.createDirectionMenu(options), ('weight', 20, False))

    def updateActionMenu(self, options):
        self.walker[0].contents[1] = (self.createActionMenu(options), ('weight', 20, False))

    def updateStats(self, newText):
        self._statText.set_text(newText)
