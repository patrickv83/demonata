""" room module """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Room(object):
    """ Room Constructor
        Precondition: Takes an x and y coordinate (type int) for the location within the world
        Postcondition: Returns a room """

    def __init__(self, x, y, text):
        # x- and y-coordinates
        self.x = x
        self.y = y
        self._text = text

    
    def getText(self):
        """ getText prints the room description
            Preconditions: None
            Postcondition: Returns the room description to the caller
            Return Type: String """
        return self._text[0]

    def updateText(self, text):
        """ updateText updates the text for the room
            Preconditions: takes text as a parameter (type string)
            Postconditions: updates description of room"""
        self._text[0] = text

    def modifyPlayer(self, player):
        """ modifyPlayer perfoms any changes to the player character within the room (if any)
            Precondition: current player object is passed to the function
            Postcondition: Player object is modified appropriately
            Return Type: Void """
        pass

    def getCoords(self):
        """ Postcondition: Returns the room coordinates in a tuple """
        return (self.x, self.y)
