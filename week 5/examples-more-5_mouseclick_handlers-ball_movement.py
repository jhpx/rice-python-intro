# Mouseclick Handlers
# Ball Movement


# This program allows the user to move a circle around the 
#	canvas using the mouse.

import simplegui

# Global Variables

canvas_width = 300
canvas_height = 300
point = [canvas_width / 2, canvas_height / 2]

# Event Handlers
        
def draw(canvas):
    canvas.draw_circle(point, 20, 5, "White", "Red")
    
# This is the handler for mouse drag events. Note that it
#	must take one parameter, a tuple of the position of the
#	mouse click.
def drag(pos):
    global point
    point = pos
    
# Frame

frame = simplegui.create_frame("Ball Drag", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
# This is necessary to tell the program what to do with
#	mouse drag events
frame.set_mousedrag_handler(drag)

# Start
frame.start()