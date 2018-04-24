""" This is the main view for demonata, with a description field on top (with optional mini map)
and a dynamically generated player actions menu on the bottom """
import urwid

from src.view.button import ActionButton

class GameView(object):
    """ The GameView class"""
    def __init__(self, descriptionText, mapText, **kwargs):
        # Room description stuff
        self.description = urwid.Filler(urwid.Text(descriptionText),
                                        valign='middle', height='pack')

        # Map stuff
        self._mapText = mapText
        self.miniMap = urwid.Pile([])

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



        self._top = urwid.Overlay(self.miniMap, self.description, align='right',
                            height=('relative', 10), valign='top',
                            width=('relative', 10), min_width=20, min_height=10)
        self.screen = urwid.Frame(self.description, header=None, footer=self.menu, focus_part='footer')

    def showMap(self):
        self.screen.contents['body'] = (self._top, None)

    def hideMap(self):
        self.screen.contents['body'] = (self.description, None)

    def toggleMap(self):
        if isinstance(self.miniMap, urwid.graphics.LineBox):
            self.hideMap()
        else:
            self.showMap()

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

    def updateMap(self, text):
        self._mapText = text
        if isinstance(self.miniMap, urwid.graphics.LineBox):
            self.miniMap.original_widget.original_widget.set_text(text)
