# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    def next_center(self):
        return [self.center[0]+self.size[0],self.center[1]]
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.thrust_image_center = info.next_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if(self.thrust):
            canvas.draw_image(self.image,self.thrust_image_center,self.image_size,self.pos,self.image_size, self.angle)
        else:
            canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size, self.angle)

    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        
        self.pos[0]%=width
        self.pos[1]%=height
        
        self.vel[0]*=0.95
        self.vel[1]*=0.95
        
        self.angle+=self.angle_vel
        
        forward = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0]+=forward[0]
            self.vel[1]+=forward[1]
    
    def set_thrust(self,thrust):
        self.thrust = thrust
    def set_angle_vel(self,angle_vel):
        self.angle_vel = angle_vel
    def get_angle_vel(self):
        return self.angle_vel
        
    def shoot(self):
        global a_missile
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0]+self.radius*forward[0],
            self.pos[1]+self.radius*forward[1]]
        a_missile = Sprite(missile_pos,[self.vel[0]+2*forward[0],self.vel[1]+2*forward[1]], self.angle, 0, missile_image, missile_info, missile_sound)
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size, self.angle)
        pass
    
    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.pos[0]%=width
        self.pos[1]%=height
        self.angle+=self.angle_vel
        pass        


def draw(canvas):
    global time
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])

    canvas.draw_text("lives:"+str(lives),[30,30],14,"White")
    canvas.draw_text("score:"+str(score),[width-100,30],14,"White")
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    a_rock = Sprite([random.randrange(0,width),random.randrange(0,height)], [random.randint(-1,1),random.randint(-1,1)], 0, 
        random.randint(-1,1)/10, asteroid_image, asteroid_info)
    pass

# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship and two sprites
my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([width / 3, height / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * width / 3, 2 * height / 3], [-1,1], 0, 0, missile_image, missile_info)

def keydown(key):
    if key==simplegui.KEY_MAP["up"]:
        my_ship.set_thrust(True)
        ship_thrust_sound.play()
    elif  key==simplegui.KEY_MAP["left"]:
        my_ship.set_angle_vel(my_ship.get_angle_vel()-0.1)
    elif  key==simplegui.KEY_MAP["right"]:
        my_ship.set_angle_vel(my_ship.get_angle_vel()+0.1)
    elif  key==simplegui.KEY_MAP["space"]:
       pass
def keyup(key):
    acc = 5
    if key==simplegui.KEY_MAP["up"]:
        my_ship.set_thrust(False)
        ship_thrust_sound.rewind()
    elif  key==simplegui.KEY_MAP["left"]:
        my_ship.set_angle_vel(0)
    elif  key==simplegui.KEY_MAP["right"]:
        my_ship.set_angle_vel(0)
    elif  key==simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        
        
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
