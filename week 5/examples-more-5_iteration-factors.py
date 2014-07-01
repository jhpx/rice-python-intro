# Iteration
# Factors


# This prints all of the factors of an input number

import simplegui

# Global Variables

canvas_width = 100
canvas_height = 100

# Event Handlers
        
def calculate(text):
    if text.isdigit() and int(text) != 0:
        num = int(text)
        # Zero is not a factor
        possible_factors = range(1, num + 1)
        answer = []
        for n in possible_factors:
            if num % n == 0:
                answer.append(n)
        print "Factors: " + str(answer)
    else:
        print "Error: Please enter a counting number (integer greater than 0)"
    
# Frame

frame = simplegui.create_frame("Factors", canvas_width, canvas_height) 
frame.add_input("Enter a counting number:", calculate, 100)

# Start
frame.start()