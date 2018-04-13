#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Room(object):
    
    # Room Constructor
    # Precondition: Takes an x and y coordinate (type int) for the location of the room within the world
    # Postcondition: Returns a room
    def __init__(self, x, y):
        # x- and y-coordinates 
        self.x = x
        self.y = y

    # generateDescription prints the room description
    # Preconditions: None
    # Postcondition: Prints the room description to the screen
    # Return Type: Void
    def introText(self):
        return

    # modifyPlayer perfoms any changes to the player character within the room (if any)
    # Precondition: current player object is passed to the function
    # Postcondition: Player object is modified appropriately
    # Return Type: Void
    def modifyPlayer(self, player):
        pass

    # Postcondition: Returns the room coordinates in a tuple
    def getCoords(self):
        return (self.x, self.y)
