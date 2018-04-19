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
        if self._mapText: self.showMap()

        directions = kwargs['directions']
        actions = kwargs.pop('actions', None)
        gameOpts = kwargs.pop('gameOpts', None)
        self._controller = kwargs.pop('controller', None)

        # Menu stuff
        actionMenu = urwid.Pile([ActionButton(action, self._controller.actionCallback)
                                 for action in actions])
        optionMenu = urwid.Pile([ActionButton(opt, self._controller.optionCallback)
                                 for opt in gameOpts])
        self.walker = urwid.SimpleFocusListWalker([])
        cols = urwid.Columns([('weight', 20, self.createDirectionMenu(directions)),
                              ('weight', 40, actionMenu),
                              ('weight', 30, optionMenu)], dividechars=2)
        self.walker.append(cols)
        self.menu = urwid.BoxAdapter(urwid.ListBox(self.walker), 6)



        top = urwid.Overlay(self.miniMap, self.description, align='right',
                            height=('relative', 10), valign='top',
                            width=('relative', 10), min_width=20, min_height=10)
        self.screen = urwid.Frame(top, header=None, footer=self.menu, focus_part='footer')

    def showMap(self):
        self.miniMap = urwid.LineBox(urwid.Filler(urwid.Text(self._mapText), valign='middle',
                                                  height='pack'))

    def hideMap(self):
        self.miniMap = urwid.Filler(urwid.Text(""), valign='middle',
                                    height='pack')

    def toggleMap(self):
        if isinstance(self.miniMap, urwid.graphics.LineBox):
            self.hideMap()
        else:
            self.showMap()

    def updateDescription(self, newText):
        self.description.base_widget.set_text(newText)

    def createDirectionMenu(self, directions):
        return urwid.Pile([ActionButton(direction, self._controller.moveCallback)
                           for direction in directions])

    def updateMap(self, text):
        self._mapText = text
        if isinstance(self.miniMap, urwid.graphics.LineBox):
            self.miniMap.original_widget.original_widget.set_text(text)
