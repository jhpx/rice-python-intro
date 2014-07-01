# Collisions
# Balloon Pop
 
 
# This program demonstrates object-object collisions. The
#	user inputs angle and velocity values for the projectile,
#	then fires it in an attempt to hit the target.
# For a challenge, you can upgrade the program so there are
#	circular obstacles you must go around. Good luck!
# Note: The angles should be entered in degrees from the bottom
#	of the screen.
 
import simplegui
import math
import random
 
# Global Variables
 
canvas_width = 900
canvas_height = 600

started = False

consecutive = 0
starting_vel = 0
starting_angle = 0

dart_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/week8-dart.png")
 
# Classes
 
class Dart:
    def __init__(self, image, image_center, image_size, radius, pos, angle, circle):
        self.image = image
        self.image_center = image_center
        self.image_size = image_size
        self.radius = radius
        self.pos = pos
        # self.circle is a boolean that tells the dart whether or
        #	not it should draw a circle around itself. Drawing 
        #	the circle makes seeing the collisions a bit easier.
        self.circle = circle
        
        self.vel = [0, 0]
        self.gravity = .1
        
    def __str__(self):
        a = "Dart" + "\n"
        a += "Image: " + str(self.image) + "\n"
        a += "Image Center: " + str(self.image_center) + "\n"
        a += "Image Size: " + str(self.image_size) + "\n"
        a += "Radius: " + str(self.radius) + "\n"
        a += "Position: " + str(self.pos) + "\n"
        a += "Velocity: " + str(self.vel) + "\n"
        a += "Angle: " + str(self.angle) + "\n"
        a += "Circle: " + str(self.circle) + "\n"
        return a
        
    def draw(self, canvas):
        if self.circle:
            canvas.draw_circle(self.pos, self.radius, 2, "Black", "White")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size)
     
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[1] += self.gravity
        
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def get_circle(self):
        return self.circle
        
    def set_pos(self, p):
        self.pos = p
        
    def set_vel(self, v):
        self.vel = v
        
    def set_circle(self, c):
        self.circle = c
        
class Balloon:
    def __init__(self, radius, color, center, canvas_height):
        self.radius = radius
        self.color = color
        self.center = center
        self.canvas_height = canvas_height
    
    def __str__(self):
        a = "Balloon" + "\n"
        a += "Radius: " + str(self.radius) + "\n"
        a += "Color: " + str(self.color) + "\n"
        a += "Center: " + str(self.center) + "\n"
        return a
    
    def draw(self, canvas):
        canvas.draw_line([self.center[0], canvas_height], self.center, 2, "Black")
        canvas.draw_polygon([(self.center[0], self.center[1] + self.radius), (self.center[0] - 10, self.center[1] + self.radius + 10), (self.center[0] + 10, self.center[1] + self.radius + 10)], 1, "Black", self.color)
        canvas.draw_circle(self.center, self.radius, 1, "Black", self.color)
        
    def get_center(self):
        return self.center
    
    def get_radius(self):
        return self.radius

# Helper Functions

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Two objects collide if the distance between their
#	centers is less than the sum of their radii.
def collide(center1, center2, radius1, radius2):
    if distance(center1, center2) < (radius1 + radius2):
        return True
    else:
        return False
    
def get_vel(magnitude, angle):
    return [magnitude * math.cos(angle), magnitude * math.sin(angle)]

def get_random_pos(radius):
    max_x = canvas_width - radius
    min_x = canvas_width // 4 + radius
    max_y = canvas_height - radius
    min_y = radius
    x = random.random() * (max_x - min_x) + min_x
    y = random.random() * (max_y - min_y) + min_y
    return [x, y]

def get_balloon():
    r = random.random() * 30 + 30
    c = random.choice(["Red", "Yellow", "Lime", "Fuchsia", "Blue"])
    p = get_random_pos(r)
    return Balloon(r, c, p, canvas_height)
    
# Event Handlers
        
def draw(canvas):
    global started, starting_vel, consecutive

    canvas.draw_text("Consecutive: " + str(consecutive), [25, 50], 30, "White")
    
    balloon.draw(canvas)
    dart.draw(canvas)
    
    if started:
        dart.update()
        if collide(dart.get_pos(), balloon.get_center(), dart.get_radius(), balloon.get_radius()):
            consecutive += 1
            reset()
        elif dart.get_pos()[1] > canvas_height:
            consecutive = 0
            reset()

def set_starting_vel(text):
    global starting_vel
    if text.isdigit():
        starting_vel = int(text)
    else:
        print "Error: Invalid starting velocity."

def set_starting_angle(text):
    global starting_angle
    if text.isdigit():
        starting_angle = math.radians(-int(text))
    else:
        print "Error: Invalid starting angle."
        
def launch():
    global started
    print starting_vel, starting_angle
    print get_vel(starting_vel, starting_angle)
    dart.set_vel(get_vel(starting_vel, starting_angle))
    started = True
    
def toggle_circle():
    dart.set_circle(not dart.get_circle())
    
def reset():
    global balloon, started
    started = False
    dart.set_pos([25, canvas_height - 25])
    dart.set_vel([0, 0])
    if consecutive != 0:
        balloon = get_balloon()
    
    
# Frame and Classes

balloon = get_balloon()
dart = Dart(dart_image, [25, 25], [50, 50], math.sqrt(25 ** 2 + 25 ** 2), [25, canvas_height - 25], 0, False)

frame = simplegui.create_frame("Curling", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_canvas_background("Aqua")
frame.add_input("Starting speed:", set_starting_vel, 200)
frame.add_input("Starting angle in degrees:", set_starting_angle, 200)
frame.add_label("Remember to hit enter above", 200)
frame.add_button("Launch!", launch, 200)
frame.add_button("Toggle Circle", toggle_circle, 200)
frame.add_button("Reset", reset, 200)

# Start
frame.start()