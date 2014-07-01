# implementation of card game - Memory

import simplegui
import random

deck = [str(i//2) for i in range(16)]

# helper function to initialize globals
def init():
    global deck,state,exposed,first_index,second_index,counter
    state = 0
    random.shuffle(deck)
    exposed  = [False]*16
    first_index = None
    second_index = None
    counter = 0
    
# define event handlers
def mouseclick(pos):
    global state,first_index,second_index,counter
    index = pos[0]//50
    if exposed[index]==False:
        exposed[index]=True
    else:
        return    
    if state==0:
        state = 1
        first_index = index
        counter+=1
    elif state==1:
        state = 2
        second_index = index
    else:
        state = 1
        if deck[first_index]!=deck[second_index]:
            exposed[first_index]=False
            exposed[second_index]=False
        first_index = index
        counter+=1
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(0,16):
        if exposed[n]:
            canvas.draw_text(deck[n],[50*n+10,65],40,"White")
        else:
            canvas.draw_polygon([(50*n, 0), (50*n, 100), (50*(n+1), 100),(50*(n+1),0)], 2, "brown","Green")
    l.set_text("Moves = "+str(counter))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric