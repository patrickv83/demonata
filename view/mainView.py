import urwid
from button import ActionButton

# Topmost widget
# inner widget depth1 - description
# inner widget depth1 - menu

class gameView(object):
    def __init__(self, descriptionText, mapText, menuChoices):
        self.__walker = urwid.SimpleFocusListWalker([])
        menu = urwid.BoxAdapter(urwid.ListBox(self.__walker), 6)
        self.__mapText = mapText
        self.__showMap()
        description = urwid.Filler(urwid.Text(descriptionText), 
                            valign='middle', height='pack')
        top = urwid.Overlay(self.miniMap, description, align='right', 
                    height=('relative', 10), valign='top', 
                    width=('relative', 10), min_width=20, min_height=10)
        body = [top, menu]
        self.screen = urwid.Frame(top, header=None, footer=menu, focus_part='footer')
        self.__createMenu(menuChoices)

    def __showMap(self):
        self.miniMap = urwid.LineBox(urwid.Filler(urwid.Text(self.__mapText), valign='middle', 
                                        height='pack'))

    def __hideMap(self):
        self.miniMap = urwid.Filler(urwid.Text(""), valign='middle', 
                                        height='pack')

    def __toggleMap(self):
        if type(self.miniMap) is urwid.graphics.LineBox:
            self._hideMap()
        else: 
            self._showMap()
        
        
    def __createMenu(self, choices):

        ActionButtonList = [ActionButton(choices[i], self.__callback) for i in range(len(choices))]
        self.__walker.append(urwid.Pile(ActionButtonList))

    def updateMenu(self, choices = list()):
        self.__walker = urwid.SimpleFocusListWalker([])
        self.createMenu(choices)

    def __callback(self, button):
        raise urwid.ExitMainLoop()

    def updateMap(self, text):
        self.__mapText = text
        if type(self.miniMap) is urwid.graphics.LineBox:
            self.miniMap._get_original_widget()._get_original_widget().set_text(text)
        

if __name__ == '__main__':
    view = gameView('Main game text', "Map", ['Choice1', 'Choice2', 'Choice3'])
    urwid.MainLoop(view.screen, palette=[('reversed', 'standout', '')]).run()
