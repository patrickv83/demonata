import sys, utils
from os import system
from testPlayer import testPlayer
from time import sleep

class game(object):

    def __init__(self):
        self.player = testPlayer()

        self.text = utils.loadFile('data/world.csv')

        self._intro()
        self._mainWindow()

    def _intro(self):
        # TODO: Set up curses color pairs so we can fade the intro text in and out
        print self.text['00'][0]
        #sleep(3)

        continueString = "(Press any key to continue)"
        p = raw_input(continueString)
        system('clear')

        print self.text['00'][1]
        p = raw_input("Something")

    def _mainWindow(self):

        un = system('clear')
        print self.text['00'][2]
        raw_input("Press enter")
        
        self.player.move_north()
        self.player.move_north()
        self.player.move_north()
        self.player.move_north()
        self.player.move_west()
        self.player.move_west()
        self.player.move_west()
        self.player.move_west()
        self.player.move_west()
        self.player.move_north()
        x, y = self.player.getLocation()

        system('clear')
        print "x = {0}, y = {1}".format(x, y)
        description = self.text['{0}{1}'.format(self.player.x, self.player.y)][0]
        print description
        raw_input("The end")
 
#        while True:
#            p = raw_input
#            system('clear')
#            description = self.text['{0}{1}'.format(self.player.x, self.player.y)][0]
#            print description
            

    
if __name__ == '__main__':
    newGame = game()
