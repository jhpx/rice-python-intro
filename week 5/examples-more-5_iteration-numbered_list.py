# Iteration
# Numbered List


# This program prints a list containing items input by the
#	user and numbers each item in the list.

import simplegui

# Global Variables

canvas_width = 100
canvas_height = 200
a_list = []

# Event Handlers
        
def add_item(text):
    a_list.append(text)
    
def print_list():
    if len(a_list) == 0:
        print "The list is empty!"
        print
    else:
	    # For every number from 0 to the length of the list
		#	(stored in the variable i)
        for i in range(len(a_list)):
            # To start the list numbers from 1, (i + 1) must
            #	be printed instead of i.
            print str(i + 1) + ". " + str(a_list[i])
        print
        
def clear_list():
    global a_list
    a_list = []
    
# Frame

frame = simplegui.create_frame("Backgrounds", canvas_width, canvas_height) 
frame.add_input("Add Item", add_item, 100)
frame.add_button("Print List", print_list, 100)
frame.add_button("Clear List", clear_list, 100)

# Start
frame.start()