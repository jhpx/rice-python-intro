# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
remain_guess =7
obj_num = 0

# helper function to initial game
def init():
    global obj_num,remain_guess
    remain_guess = math.ceil(math.log(num_range)/math.log(2))
    obj_num = random.randrange(0,num_range)
    print "New game, Range is from 0 to",num_range
    print "Number of remaining guesses is",remain_guess
    print

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range,remain_guess
    num_range = 100
    init()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range,remain_guess
    num_range = 1000
    init()
    
def get_input(guess):
    # main game logic goes here	
    print "Guess was",guess
    
    global remain_guess
    remain_guess -=1
    
    print "Number of remaining guesses is",remain_guess
    
    if(int(guess)==obj_num):
        print "Correct!\n"
        init()
    elif(remain_guess<=0):
        print "You ran out of guesses. The number was",obj_num,"\n"
        init()
    elif(int(guess)>obj_num):
        print "Higher!\n"
    else:
        print "Lower!\n"

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

init()

# start frame
f.start()

# always remember to check your completed program against the grading rubric
