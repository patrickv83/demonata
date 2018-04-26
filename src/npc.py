""" NPC Module
    Defines NPC for special rooms """
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from src.character import Character

class NPC(Character):
    """ NPC superclass creates an NPC for special rooms """
    def __init__(self, name, hp):
        """@ReturnType NPC"""
        super(NPC, self).__init__(name, hp)
    def react(option):
        pass

class Tutor(NPC):
    def __init__(self):
        super(Tutor, self).__init__(name = "Tutor", hp = 5)

    def react(option):
        if option == 1:
            reaction = "You chose poorly."
        elif option == 2:
            reaction = "This option doesn't get you any good info."
        elif option == 3:
            reaction = "There you go! I saw the teaching assistant running down the street. Looks like he was headed to the bar."
        else:    # Invalid option
            reaction = "I don't understand, try again."

        return reaction

class Bartender(NPC):
    def __init__(self):
        super(Bartender, self).__init__(name = "Bartender", hp = 5)

    def react(option):
        # Bartender's reactions to interrogation
        if option == 1: 
            reaction = "I might have seen something."
        elif option == 2: 
            reaction = "I think assistant went to the bookstore. Or was it the grocery store? Maybe it was both."
        elif option == 3:
            reaction = "What teaching assistant?"
        else:    # Invalid option
            reaction = "I don't understand, try again."

        return reaction

class Bookworm(NPC):
    def __init__(self):
        super(Bookworm, self).__init__(name = "Bookworm", hp = 5)

    def react(option):
        # Bookworm tells player what the assistant purchased
        if option == 1:
            reaction = "I can't tell you that, I could get fired."
        elif option == 2:
            reaction = "That teaching assistant could use some sun."
        elif option == 3:
            reaction = "Ok, I'm really not supposed to do this, but the teaching assistant came in and purchased a copy of 'Advanced Demon Summoning.' Do you think he is really going to do it, summon a demon?"
        else:    # Invalid option
            reaction = "I don't understand, try again."

        return reaction

class Cashier(NPC):
    def __init__(self):
        super(Cashier, self).__init__(name = "Cashier", hp = 5)

    def react(option):
        # Cashier tells player what the assistant purchased
        if option == 1: 
            reaction = "He bought fifteen pounds of raw meat and some black candles. What an odd combination."
        elif option == 2:
            reaction = "I have to feed my cats. I can't get fired from this job."
        elif option == 3:
            reaction = "Do you want to see a picture of my cats? They are the cutest!"
        else:    # Invalid option
            reaction = "I don't understand, try again."

        return reaction
