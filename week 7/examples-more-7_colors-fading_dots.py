# Colors
# Fading Dots


# This program draws randomly colored fading dots that are
#	placed by the mouse clicks of the user.  

import simplegui
import random

# Global Variables

canvas_width = 300
canvas_height = 300
dots = []


# Classes for colors and dots


class RGBcolor:
    
    # create color with specified intensities
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    # make HTML color string
    def make_html(self):
        return "rgb(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"
    
    # print out readable representation
    def __str__(self):
        return "Red: " + str(self.red) + ", Green: " + str(self.green) + ", Blue: " + str(self.blue)
    
    # brighten towards white
    def brighten(self):
        self.red += 1
        self.green += 1
        self.blue += 1
        
class Dot:
    def __init__(self, pos, color, radius, lifespan):
        self.pos = pos
        self.color = color
        self.radius = radius
        # Without lifespan, the number of dots would increase
        #	indefinitely, causing the program to slow down.
        self.life = lifespan
        
    def draw(self, canvas):
        color_string = self.color.make_html()
        canvas.draw_circle(self.pos, self.radius, 1, color_string, color_string)
        
    # Updates the life and causes the color to fade to white.
    def update(self):
        self.life -= 1
        self.color.brighten()
        
    def get_life(self):
        return self.life


# Event Handlers
        
def draw(canvas):
    # Iterate over list(dots) instead of dots, to make a copy.
    # This allows you to safely remove from dots inside the loop.
    for d in list(dots):
        d.update()
        d.draw(canvas)

        # Remove dot if it's too old
        if d.life <= 0:
            dots.remove(d)
 
def click(pos):
    new_color = RGBcolor(random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    print new_color
    print "HTML color is " + new_color.make_html()
    print
    dots.append(Dot(pos, new_color, 20, 256))
    
# Frame

frame = simplegui.create_frame("Fading Dots", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("White")

# Start
frame.start()