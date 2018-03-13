#ex 35: Branches and Functions
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    next = input("> ")
    if("0"in next or "1" in next):
        how_much = int(next)
    else:
        dead("Man learn to type a number")
    if(how_much < 50):
        print("Nice! You're not greedy, you win!")
    else:
        print("You greedy ass!")

def bear_room():
    print("There is a bear here")
    print("The bear has bunch of money")
    print("The fat feat is in front of another door")
    print("How are you going to move the dear")
    bear_moved = False
    while True:
        next = input("> ")
        if(next == "take honey"):
            dead("The bear looks at your face and then slaps it")
        elif (next == "taunt bear" and bear_moved):
            dead("The bear gets pissed off and chews your legs off!")
        elif (next == "open door"and bear_moved):
            gold_room()
        else:
            print("I have got no idea what that means")

def cthulu_room():
    print("Here you seen the great evil Cthulu")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")
    next = input( "> ")
    if("flee" in next):
        start()
    elif("head" in next):
        dead("Well! that was tasty")
    else:
        cthulu_room()

def dead(why):
    print(why, "Good Job")
    exit(0)

def start():
    print("You are in the dark room")
    print("Their is a door to take you left and right")
    print("Which one would you take")
    next = input("> ")
    if(next == "left"):
        bear_room()
    elif(next == "right"):
        cthulu_room()
    else:
        dead("You stumble around the room till you starve")


start()        
    
    
            
            
    
        
