""" This is the main view for demonata, with a description field on top (with optional mini map)
and a dynamically generated player actions menu on the bottom """
import urwid

from src.view.button import ActionButton
from src.world import World

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

        self._directions = kwargs['directions']
        actions = kwargs['actions']
        gameOpts = kwargs['gameOpts']
        self._controller = kwargs.pop('controller', None)

        # Menu stuff
        self._directionMenu = self.createDirectionMenu()
        actionMenu = urwid.Pile([ActionButton(action, self._actionCallback) for action in actions])
        optionMenu = urwid.Pile([ActionButton(opt, self._optionCallback) for opt in gameOpts])
        self._walker = urwid.SimpleFocusListWalker([])
        cols = urwid.Columns([('weight', 20, self._directionMenu),
                              ('weight', 40, actionMenu),
                              ('weight', 30, optionMenu)], dividechars=2)
        self._walker.append(cols)
        self.menu = urwid.BoxAdapter(urwid.ListBox(self._walker), 6)



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

    def createDirectionMenu(self):
        return urwid.Pile([ActionButton(direction, self._moveCallback) 
                           for direction in self._directions])

    def _optionCallback(self, button):
        pass

    def _actionCallback(self, button):
        pass

    def _moveCallback(self, button):
        functions = {'move_north': (self._controller.world.movePlayer, World.NORTH),
                     'move_south': (self._controller.world.movePlayer, World.SOUTH),
                     'move_east': (self._controller.world.movePlayer, World.EAST),
                     'move_west': (self._controller.world.movePlayer, World.WEST)}
        label = button._w.original_widget.text.lower().replace(' ', '_')
        if label in functions:
            functions[label][0](functions[label][1])
        self.updateDescription(self._controller.world.getDescriptionText())
        self._directions = self._controller.world.getDirectionOptions()
        self._directionMenu = self.createDirectionMenu()
        self._controller._loop.draw_screen()

    def updateMap(self, text):
        self._mapText = text
        if isinstance(self.miniMap, urwid.graphics.LineBox):
            self.miniMap.original_widget.original_widget.set_text(text)
