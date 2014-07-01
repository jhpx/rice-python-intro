# template for "Stopwatch: The Game"
import simplegui

# define global variables
watch_counter = 0
success = 0
attempts = 0
watch_status = 0

# define helper functions
def format(t):
    '''converts integer counting tenths of seconds into 
        formatted string A:BC.D'''
    D = t%10
    C = (t%100)//10
    B = (t%600)//100
    A = t//600
    return str(A)+':'+str(B)+str(C)+'.'+str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    '''click "Start" to start the stop watch'''
    global watch_status
    if(watch_status == 0):
        timer.start()
        watch_status = 1

    
def stop():
    '''click "Stop" to stop the stop watch'''
    global watch_status,attempts,success
    if(watch_status == 1):
        timer.stop()
        watch_status = 0
        attempts += 1
        if(watch_counter%10==0):
            success += 1
        
def reset():
    '''click "Reset" to reset the stop watch'''
    global watch_status,watch_counter,attempts,success
    watch_counter = 0
    attempts = 0
    success = 0
    if(watch_status == 1):
        timer.stop()
        watch_status = 0
    
# define event handler for timer with 0.1 sec interval
def count():
    '''auto increment the watch counter'''
    global watch_counter
    watch_counter += 1

    
# define event handler for drawing  
def draw(canvas):
    '''draw the stop watch in the center of canvas'''
    global watch_counter
    canvas.draw_text(format(watch_counter), [50,113], 36, "White")
    canvas.draw_text(str(success)+'/'+str(attempts),[150,35],20,"Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",200,200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, count)

# start timer and frame
frame.start()

# remember to review the grading rubric