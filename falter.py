from sys import exit
from random import randint
import tellme

class Game(object):

    def __init__(self, start):
        self.game_over = [
            "You have died.",
            "Unfortunate."
            ]
        self.start = start
    
    def play(self):
        next = self.start
        while True:
            print "\n###-----------------------------###"
            room = getattr(self, next)
            next = room()
    
    
    
    
    def cell(self):
        #Cell ~ actions (look around, eat food, sleep)
        print "You awoke in a prison cell. Dark and musty, you look around seeing a small bed and a dirty sink."
        print "A loud thud comes from the door to your cell. \"Eat up. It may be your last meal.\" a voice tells you as you get to your feet."
        print "A plate is shoved into your room through a slot. Something appears to be on it, but it doesn't look edible."
        cont = 1
        while cont == 1:
            action = raw_input("> ")
            action.lower()
            if action == "look around":
                print "There isn't much else to look at. There is your bed, a small sink, and the plate of food."
                
            elif "food" in action:
                print "food works"
                cont = 0
            elif "sleep" in action:
                print "sleep"
                cont = 0
            elif "exit" in action:
                print "Possible exit requested. Type 'confirm' to continue."
                end_game = raw_input("> ")
                end_game.lower()
                if end_game == "confirm":
                    exit(1)
                else:
                    print "Continuing game..."
                    cont = 1
            else:
                print "Command not recognized."
                cont = 1
        print "Loop exited. exiting game."
        exit(1)
        





game_instance = Game('cell')
game_instance.play()
