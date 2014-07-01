# Images
# Changes


# This program demonstrates rotations and image distortions.

import simplegui
import math

# Global Variables

canvas_width = 200
canvas_height = 200
image_center = (25, 25)
image_size = (50, 50)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/week5-triangle2.png")

# Event Handlers
        
def draw(canvas):
    # The optional last parameter is the rotation in radians.
    canvas.draw_image(image, image_center, image_size, [50, 50], image_size, 0)
    canvas.draw_image(image, image_center, image_size, [150, 50], image_size, math.pi / 2)
    canvas.draw_image(image, image_center, image_size, [150, 150], image_size, math.pi)
    canvas.draw_image(image, image_center, image_size, [50, 150], image_size, 3 * math.pi / 2)
    # Changing the second image size shrinks or enlarges the image.
    canvas.draw_image(image, image_center, image_size, [100, 100], (25, 25))
    canvas.draw_image(image, image_center, image_size, [100, 50], (25, 50), math.pi)
    canvas.draw_image(image, image_center, image_size, [100, 150], (40, 25))
    
# Frame

frame = simplegui.create_frame("Backgrounds", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_canvas_background("Maroon")

# Start
frame.start()