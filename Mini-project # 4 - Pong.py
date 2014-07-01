# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

SCORE_OFFSET_X = 60
SCORE_OFFSET_Y = 80

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if(right):
        ball_vel = [random.randint(120, 240),-random.randint(60,180)]
    else:
        ball_vel = [-random.randint(120, 240),-random.randint(60,180)]
    
    #change vel from pixel per second to pixel per update (1/60 seconds)
    ball_vel[0] /= 60.0
    ball_vel[1] /= 60.0
    
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH,HEIGHT/2]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    ball_init(random.randint(0,1)==1)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1]+=paddle1_vel[1]
    if paddle1_pos[1]<HALF_PAD_HEIGHT:
        paddle1_pos[1]=HALF_PAD_HEIGHT
    elif paddle1_pos[1]>HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos[1]=HEIGHT-HALF_PAD_HEIGHT

    paddle2_pos[1]+=paddle2_vel[1]
    if paddle2_pos[1]<HALF_PAD_HEIGHT:
        paddle2_pos[1]=HALF_PAD_HEIGHT
    elif paddle2_pos[1]>HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos[1]=HEIGHT-HALF_PAD_HEIGHT
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    leftTop1=[paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT]
    rightTop1=[paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT]
    leftBottom1=[paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT]
    rightBottom1=[paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT]
    
    leftTop2=[paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT]
    rightTop2=[paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT]
    leftBottom2=[paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT]
    rightBottom2=[paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT]
    
    c.draw_polygon([leftTop1,rightTop1,rightBottom1,leftBottom1], 1, "White", "White")
    c.draw_polygon([leftTop2,rightTop2,rightBottom2,leftBottom2], 1, "White", "White")
   
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] *= -1
    elif ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1] *= -1

    if ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        if ball_pos[1]<=paddle1_pos[1]+HALF_PAD_HEIGHT and ball_pos[1]>=paddle1_pos[1]-HALF_PAD_HEIGHT:
            ball_vel[0]*=-1.1
        else:
            score2+=1
            ball_init(True)
    elif ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS:
        if ball_pos[1]<=paddle2_pos[1]+HALF_PAD_HEIGHT and ball_pos[1]>=paddle2_pos[1]-HALF_PAD_HEIGHT:
            ball_vel[0]*=-1.1
        else:
            score1+=1
            ball_init(False)

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1),[WIDTH/2-SCORE_OFFSET_X,SCORE_OFFSET_Y],32,"White")
    c.draw_text(str(score2),[WIDTH/2+SCORE_OFFSET_X,SCORE_OFFSET_Y],32,"White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc 
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] -= acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] -= acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] += acc 


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()

