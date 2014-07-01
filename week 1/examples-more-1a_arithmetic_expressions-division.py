# Arithmetic expressions - numbers, operators, expressions
# Integer vs. Regular division


# Regular division - includes fractional part
# Single division sign
# Used to get exact values

# Ex. 1 What is one third of thirty-two?
print "Ex. 1:", 32 / 3

# Ex. 2 What is 19 / 24 as a percentage?
print "Ex. 2:", (19 / 24) * 100, "%"

# Ex. 3 What is the average of 3, 5, 17, and 29?
print "Ex. 3:",(3 + 5 + 17 + 29) / 4


print "--------"
# Integer division - evaluates to the largest whole number less than the 
#                    exact result (floor function)
# Double division sign
# Used to get whole numbers

# Ex. 4 If there are 6 triangles in a hexagon, how many complete
# 	hexagons can be made with 27 triangles?
print "Ex. 4:", 27 // 6

# Ex. 5 If 20 people can fit on each bus, how many full busses
#	will there be if 59 people are riding in busses?
print "Ex. 5:", 59 // 20

# Ex. 6 If Dan can eat one hotdog in 16 seconds, how many
#	whole hotdogs can he eat in 3 minutes?
print "Ex. 6:", (3 * 60) // 16


print "--------"
# Try changing the number of division signs in the 
# 	problems above to test it out for yourself!


# Note: Integer division is not always the same as 
#	converting a float to an integer - they round the
#	opposite directions when the result is a negative number
print "Same:", 6 // 5, int(6 / 5)
print "Same:", 0 // 3, int(0 / 3)
print "Different:", -7 // 4, int(-7 / 4)


print "--------"
# Note: Division by zero is handled differently by regular
#	and integer division.
# Try it! Uncomment the lines below to see what happens:
#print "Error:", 3 // 0
#print "Error:", 3 / 0

# It is important to make sure that division by zero does
#	not occur. The error you get can cause your game or 
#	program to end prematurely. Be especially careful when 
#	the denominator of a fraction is an arithmetic expression
#	or a changing variable.
# For example:
#print "Error:", 4 / (3 * 4 - 12)

# Although the division by zero is not obvious at first, it
#	can still kill your program. Make it a habit to always
#	check for this possibility whenever you use division.
