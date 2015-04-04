from sys import exit
from random import randint
from tellme import possible_exit
from tellme import error

class Game(object):
    
    cell_key = 0
    
    
    def __init__(self, start):
        self.game_over = [
            "You have died.",
            "Unfortunate."
            ]
        self.start = start
        
        
    def play(self):
        next = self.start
        
        while True:
            print "\n###---------------%r--------------###" % next
            
            room = getattr(self, next)
            
            next = room()
    
	def death(self):
		i = randint(0,(game_over.len)-1)
		print game_over[i]
    
    def hallway(self):
        print "The hallway you entered runs left and right. Which way do you choose?"
        direction = raw_input("> ")
        direction.lower()
        
        stealth = randint(0,10)
        cont = 1
        
        while cont == 1:
            if "left" in direction:
                print "You sprint left, trying to be as stealthy as possible."
                if stealth <= 4:
                    print "Despite your attempts, a guard hears something and comes to investigate."  
                    return "guard"
                else:
                    print "No one seems to notice you escape, and you jump through the door at the end of the hallway."
                    return "broom_closet"
            elif "right" in direction:
                print "You ran right.."
                return "guard"
            elif "exit" in direction:
                possible_exit()
            else:
                error()
    
    def broom_closet(self):
        print "Broom Closet"
        exit(1)
    
    def jail(self):
        print "Jail"
        exit(1)
    
    def caught(self):
        print "Caught"
        return "death" 
        
    
    def guard(self):
        print "You come face to face with a guard. He looks flustered. What do you do?"
        action = raw_input("> ")
        cont = 1
        while cont == 1:
            if "taunt" in action:
                print "You give the guard the finger, trying to taunt him to attack first."
                intel = randint(1,6)
                if intel > 2:
                    print intel
                    print "The guard runs at you recklessly and you are able to get a good decisive hit on him."
                    print "The guard falls on the floor where you are able to knock him out."
                    return "jail"
                else:
                    print "The guard doesn't fall for your taunt and runs straight for the intercom."
                    print "He hits the intercom button and calls for help before you can even react."
                    return "caught"
            elif "run" in action:
                print "run"
            elif "fight" in action:
                print "fight"
            elif "exit" in action:
                possible_exit()
            else:
                error()
        
        
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
            elif "sink" in action:
            	print "There isn't much to the sink, the mirror is cracked and the hot water doesn't even work."
            elif "food" in action:
                print "You go to check the plate of food and you see a key hidden among the food. You pick it up. It looks to fit the door to your cell."
                self.cell_key = 1
            elif "sleep" in action:
                print "You go to try to sleep but the cold of the room and the uncomfortable bed are enough to keep you awake."
            elif "key" in action and self.cell_key == 1:
            	print "You use the key to open the cell door. A loud thunk emnates from the door, but noone seems to have noticed."
            	next_room = "hallway"
            	return next_room
            elif "exit" in action:
                possible_exit()
            else:
                error()
        

game_instance = Game("cell")
game_instance.play()
