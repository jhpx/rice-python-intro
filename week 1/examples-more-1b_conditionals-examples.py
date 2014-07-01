# Logic and Comparisons
# Examples


# Utilizing if-elif-else statements greatly expands the types
#	of functions you can make. Note that the test cases try
#	to test all of the different possibilities.

# Absolute value

def absolute_value(num):
    if num < 0:
        num = num * -1
    return num

print "Absolute Value:", absolute_value(9)
print "Absolute Value:", absolute_value(-4)
print "Absolute Value:", absolute_value(0)
print

# Number of real solutions to a quadratic equation

def num_solutions(discriminant):
    if discriminant > 0:
        return 2
    elif discriminant < 0:
        return 0
    else:
        return 1
    
print "Number of Solutions:", num_solutions(1)
print "Number of Solutions:", num_solutions(-1)
print "Number of Solutions:", num_solutions(0)
print

# Prints the type of triangle given the largest angle 
#	measurement in degrees

def print_triangle_type(degrees):
    if degrees > 90 and degrees < 180:
        print "Triangle is obtuse!"
    elif degrees == 90:
        print "Triangle is right!"
    elif degrees < 90 and degrees > 0:
        print "Triangle is acute!"
    else:
        print "Triangle does not exist!"
        
print_triangle_type(137)
print_triangle_type(90)
print_triangle_type(54)
print_triangle_type(-1)
print_triangle_type(180)
print

# Returns True if a triangle can be made with the given 
#	side lengths, False otherwise.
#	(if the two smallest sides add up to be greater than
#	 the largest one)

def is_triangle(side_1, side_2, side_3):
    max_side = max(side_1, side_2, side_3)
    if max_side == side_1:
        return (side_2 + side_3) > side_1
    elif max_side == side_2:
        return (side_1 + side_3) > side_2
    else:
        return (side_1 + side_2) > side_3

print "Triangle:", is_triangle(3, 4, 5)
print "Triangle:", is_triangle(5, 3, 4)
print "Triangle:", is_triangle(4, 5, 3)
print "Triangle:", is_triangle(1, 1, 2)
print "Triangle:", is_triangle(5, 6, 19)




        
        
        
        
        
