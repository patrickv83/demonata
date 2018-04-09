import curses
from textwrap import fill
from time import sleep

def _initColors():
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i+1,i,-1)

    

def fadeText(text, screen, seconds = 2, y = 0, x = 0):
    '''This method fades text in for (seconds/4), displays it for (seconds/2), then fades out'''
    if screen is None: return
    
    for i in range(0,7):
        screen.refresh()
        screen.addstr(y, x, fill(text))#, curses.color_pair(i))
        sleep(seconds/32.0)
        screen.erase()

    displayText(text, screen, y, x)
    screen.refresh()
    sleep(seconds/2.0)
    screen.erase()
    for i in range(7,0):
        screen.refresh()
        screen.addstr(y, x, fill(text))#, curses.color_pair(i))
        sleep(seconds/32.0)
        screen.clear()

def displayText(text, screen, y = 5, x = 0, erase = False):
    if screen is None: return
    
    if erase is True: screen.clear()
    screen.addstr(y, x, fill(text))
    screen.refresh()
