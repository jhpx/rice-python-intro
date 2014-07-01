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

def process_sprite_group(sprite_set,canvas):
    remove_set = set([])
    for sprite in sprite_set:
        if(sprite.update()==False):
            remove_set.add(sprite)
        sprite.draw(canvas)
    sprite_set.difference_update(remove_set)  
    pass  

def group_collide(sprite_set,other_object):
    num = 0
    remove_set = set([])

    for sprite in sprite_set:
        if(sprite.collide(other_object)):
            remove_set.add(sprite)
            num+=1
            an_explosion = Sprite(sprite.get_position(), [0,0], 0, 0, explosion_image, explosion_info, explosion_sound)
            explosion_group.add(an_explosion)
    sprite_set.difference_update(remove_set)        
    return num        

def group_group_collide(sprite_set,other_object_set):
    num = 0
    remove_set = set([])
    for sprite in sprite_set:
        if(group_collide(other_object_set,sprite)>0):
            remove_set.add(sprite)
            num+=1
    sprite_set.difference_update(remove_set)        
    return num      

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
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = ship_thrust_sound
        self.forward = angle_to_vector(self.angle)
        
    def draw(self,canvas):
            canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size, self.angle)

    def update(self):
        
        self.angle+=self.angle_vel
        
        self.forward = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0]+=0.12*self.forward[0]
            self.vel[1]+=0.12*self.forward[1]
        
        self.vel[0]*=0.99
        self.vel[1]*=0.99
        
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.pos[0]%=width
        self.pos[1]%=height
    
    def thrust_on_off(self, thrust):
        self.thrust=thrust
        if self.thrust:
            self.image_center[0]+=90
            self.sound.play()
        else:
            self.image_center[0]=45
            self.sound.rewind()
        
    def rotate(self, s):
        if s=="left":
            self.angle_vel+=-0.1
        elif s=="right":
            self.angle_vel+=0.1
        elif s=="stopped":
            self.angle_vel=0
        
    def shoot(self):
        missile_pos = [self.pos[0]+self.radius*self.forward[0],
            self.pos[1]+self.radius*self.forward[1]]
        a_missile = Sprite(missile_pos,[self.vel[0]+2*self.forward[0],self.vel[1]+2*self.forward[1]], self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
        
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
    
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
        if(self.animated):
            current_center = [self.image_center[0] + self.age*self.image_size[0], self.image_center[1]]
            canvas.draw_image(self.image,current_center,self.image_size,self.pos,self.image_size, self.angle)
        else:
            canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size, self.angle)
        pass
    
    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.pos[0]%=width
        self.pos[1]%=height
        self.angle+=self.angle_vel
        self.age+=1
        return self.age<self.lifespan        

    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos
    
    def collide(self,other_object):
        return dist(self.pos,other_object.get_position())<=self.radius+other_object.get_radius()
            
def draw(canvas):
    
    global time,lives,score,started,rock_group,missile_group,explosion_group

    if(group_collide(rock_group,my_ship)):
        lives-=1
    if(lives<=0):
        started = False
        
    score+=10*group_group_collide(rock_group,missile_group)   
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
    if(started==False):
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [width/2, height/2], splash_info.get_size())
    
    canvas.draw_text("Lives", (25,40), 25, "White")
    canvas.draw_text(str(lives), (25,75), 25, "White")
    canvas.draw_text("Score", (700, 40), 25, "White")
    canvas.draw_text(str(score), (700, 75), 25, "White")
    
    # draw ship and sprites
    my_ship.draw(canvas)
    
    process_sprite_group(explosion_group,canvas)
    
    if(started):
        process_sprite_group(rock_group,canvas)
        process_sprite_group(missile_group,canvas) 
    else:
        rock_group = set([])	
        missile_group = set([])
    
        
    # update ship and sprites
    my_ship.update()
        

    
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if(len(rock_group)<12):
        a_rock = Sprite([random.randrange(0,width),random.randrange(0,height)], [random.randint(-1,1),random.randint(-1,1)], 0, random.randint(-1,1)/10, asteroid_image, asteroid_info)
        while(a_rock.collide(my_ship)==True):
            a_rock = Sprite([random.randrange(0,width),random.randrange(0,height)], [random.randint(-1,1),random.randint(-1,1)], 0, random.randint(-1,1)/10, asteroid_image, asteroid_info)
        rock_group.add(a_rock)
    pass

        
    
# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship and two sprites
my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])
started = False

def keydown(key):
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust_on_off(True)
    elif  key==simplegui.KEY_MAP["left"]:
        my_ship.rotate("left")
    elif  key==simplegui.KEY_MAP["right"]:
        my_ship.rotate("right")
    elif  key==simplegui.KEY_MAP["space"]:
        my_ship.shoot()

        
def keyup(key):
    acc = 5
    if key==simplegui.KEY_MAP["up"]:
        my_ship.thrust_on_off(False)
    elif  key==simplegui.KEY_MAP["left"]:
        my_ship.rotate("stopped")
    elif  key==simplegui.KEY_MAP["right"]:
        my_ship.rotate("stopped")
        
def mouse_handler(pos):
    global started,lives,score
    if(started==False):
        started = True
        lives = 3
        score =0
        soundtrack.play()
        explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouse_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
