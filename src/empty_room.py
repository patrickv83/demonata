#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.room import Room

class EmptyRoom(Room):
    # EmptyRoom Constructor
    # Precondition: takes an x-, y-coordinates and a description
    def __init__(self, x, y, desc):
        self.description = desc
        super().__init__(x, y)

    # introText prints the room description
    def introText(self):
        print self.description

    # modifyPlayer
    # EmptyRoom objects have no player modifications
    def modifyPlayer(self, player):
        pass

    # getCoordinates
    # Postcondition: returns coordinates of room in tuple
    def getCoordinates(self):
        return (self.x, self.y)
