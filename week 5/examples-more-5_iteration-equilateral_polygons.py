# Iteration
# Equilateral Polygons


# This program draws equilateral polygons using a loop.

import simplegui
import math

# Global Variables

canvas_width = 300
canvas_height = 300
num_sides = 3
angle = 0
radius = 150

# Event Handlers
        
def draw(canvas):
    points = []
    # This formula returns equally spaced points on a circle
    #	which, if connected, form an equilateral polygon.
    for i in range(num_sides):
        a = (math.pi * 2 / num_sides) * i + angle
        p = [canvas_width / 2 + math.cos(a) * radius / 3, canvas_height / 2 + math.sin(a) * radius / 3]
        points.append(p)
    canvas.draw_polygon(points, 3, "White", "Aqua")
 
def set_num_sides(text):
    global num_sides
    if text.isdigit() and int(text) >= 3:
        num_sides = int(text)
    else:
        print "Error: invalid number of sides"
        
# The angle is entered in degrees and converted to radians
def set_angle(text):
    global angle
    if text.isdigit():
        angle = int(text) / 360 * 2 * math.pi
    else:
        print "Error: invalid angle"
    
# Frame

frame = simplegui.create_frame("Equilateral Polygons", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.add_input("Number of sides:", set_num_sides, 100)
frame.add_input("Angle:", set_angle, 100)

# Start
frame.start()