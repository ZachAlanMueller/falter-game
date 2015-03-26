from sys import exit
from random import randint
from tellme import possible_exit

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
	
	def death(self):
		i = randint(0,(game_over.len)-1)
		print game_over[i]
	
	def hallway(self):
		print "Hallway dialogue.."
		    
    def cell(self):
        #Cell ~ actions (look around, eat food, sleep)
        print "You awoke in a prison cell. Dark and musty, you look around seeing a small bed and a dirty sink."
        print "A loud thud comes from the door to your cell. \"Eat up. It may be your last meal.\" a voice tells you as you get to your feet."
        print "A plate is shoved into your room through a slot. Something appears to be on it, but it doesn't look edible."
        cont = 1
        has_key = 0
        while cont == 1:
            action = raw_input("> ")
            action.lower()
            if action == "look around":
                print "There isn't much else to look at. There is your bed, a small sink, and the plate of food."
            elif "sink" in action:
            	print "There isn't much to the sink, the mirror is cracked and the hot water doesn't even work."
            elif "food" in action:
                print "You go to check the plate of food and you see a key hidden among the food. You pick it up. It looks to fit the door to your cell."
                has_key = 1
            elif "sleep" in action:
                print "You go to try to sleep but the cold of the room and the uncomfortable bed are enough to keep you awake."
            elif "key" in action and has_key == 1:
            	print "You use the key to open the cell door. A loud thunk emnates from the door, but noone seems to have noticed."
            	return "hallway"
            elif "exit" in action:
                possible_exit()
            else:
                print "Command not recognized."
                cont = 1
        

		




game_instance = Game('cell')
game_instance.play()
