import sys
import curses
from gameMenu import Menu
from World import World
import Player
import utils
from textwrap import fill
from time import sleep

class gameWindow(object):

    def __init__(self, screen):
        self.currentX = 0
        self.currentY = 0
        self.player = Player.Player("TestPlayer", 40, gold = 100)
        self.screen = screen
        curses.curs_set(0)

        screen.clear()
        self.currentY, self.currentX = screen.getmaxyx()
        self.descY = int(self.currentY * .5)
        self.descriptionPanel = screen.subwin(self.descY, self.currentX, 0, 0)
        self.playerMenuPanel = screen.subwin(self.descY+1, 0)
        self.text = World().getRooms()

        self._intro(screen)
        #self._mainWindow(screen)

    def _intro(self, screen):
        screen.clear()
        # TODO: Set up curses color pairs so we can fade the intro text in and out
        self.descriptionPanel.addstr(5, 0, fill(self.text['00'][0]))
        self.descriptionPanel.refresh()
        sleep(3)
        #for i in range(0, 5):
        #    sleep(0.7)
        #    curses.flash()
        #    sleep(0.3)
        #    curses.flash()
        continueString = "(Press any key to continue)"
        utils.displayText(continueString, self.descriptionPanel, self.descY - 5, int((self.currentX - len(continueString))/2), erase = False)
        self.descriptionPanel.getch()
        utils.displayText(self.text['00'][1], self.descriptionPanel, 5, 0, erase=True)

        introMenuItems = [ 
                            ('Answer the phone', self._mainWindow),
                            ('Ignore it - it can\'t be that important', self._loseImmediately) 
        ]
        introMenu = Menu(introMenuItems, self.playerMenuPanel)
        introMenu.display()
        self.playerMenuPanel.refresh()
        self.descriptionPanel.refresh()

        while True:
            c = self.screen.getch()

    def _mainWindow(self):

        utils.displayText(self.text['00'][2], self.descriptionPanel, 5, 0, erase = True)
    
        

        while True:
            x, y = self.player.getLocation()
            menuItems = []

            # TODO: Move this logic into room class with accessor function to test if you can move a certain direction
            for direction in ['north', 'south', 'east', 'west']:
                try:
                    deltaX, deltaY = getattr(Player, direction.upper())
                    s = x + deltaX
                    t = y + deltaY
                    self.text['{0}{1}'.format(s, t)]
                    menuItems.append(('Move {0}'.format(direction), getattr(self.player, "move_{0}".format(direction))))

                except KeyError:
                    continue
            #menuItems.append(("Search", self.player.search)) if room.hasItem()
            menuItems.append(("Save and exit", sys.exit))
            playerMenu = Menu(menuItems, self.playerMenuPanel)
            playerMenu.display()

            with open('debug.log', 'a') as file:
                file.write("before getch")
            c = self.screen.getch()
            with open('debug.log', 'a') as file:
                file.write("after getch")
            description = self.text['{0}{1}'.format(self.player.x, self.player.y)][0]
            utils.displayText(description, self.descriptionPanel, erase = True)
            playerMenu = None
            




    def _loseImmediately(self):
        text1 = 'Ignoring your better judgment, you leave the phone on your desk and it eventually stops ringing. If it was important they would call back - and they don\'t, so it must not have been important...'
        text2 = 'The nagging feeling at the back of your brain sticks around for a couple days - until the hellmouth opens up a couple streets over and legions of demons pour out. Now all other worries are overshadowed by the concern that you\'ll be eaten by a demon. Game over.'
        utils.displayText(text1, self.descriptionPanel, 5, 0, erase = True)
        sleep(5)
        utils.displayText(text2, self.descriptionPanel, 8, 0)
        sleep(3)
        self.screen.getch()
        sys.exit(0)
    
if __name__ == '__main__':
    curses.wrapper(gameWindow)
