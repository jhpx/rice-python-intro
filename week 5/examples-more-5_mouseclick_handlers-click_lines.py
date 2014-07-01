# Mouseclick Handlers
# Click Lines


# This program allows the user to draw a line between two
#	mouse clicks

import simplegui

# Global Variables

canvas_width = 300
canvas_height = 300
points = [(canvas_width / 2, canvas_height / 2)]

# Event Handlers
        
def draw(canvas):
    canvas.draw_polyline(points, 5, "White")
  
def reset():
    global points
    p = points[-1]
    points = [p]
      
# This is the handler for mouse click events. Note that it
#	must take one parameter, a tuple of the position of the
#	mouse click.
def click(pos):
    if pos != points[-1]:
        points.append(pos)
        print "Next point:", pos
    
# Frame

frame = simplegui.create_frame("Click Lines", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
# This is necessary to tell the program what to do with
#	mouse click events
frame.set_mouseclick_handler(click)
frame.add_button("Reset", reset)

# Start
frame.start()