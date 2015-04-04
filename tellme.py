def possible_exit():
    print "Possible exit requested. Type 'confirm' to continue."
    end_game = raw_input("> ")
    end_game.lower()
    if end_game == "confirm":
    	print "\nExiting Game.\n"
        exit(1)
    else:
        print "Continuing game..."

def error():
    print "Command not recognized."
