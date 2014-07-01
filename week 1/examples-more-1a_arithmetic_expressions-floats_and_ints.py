# Arithmetic expressions - numbers, operators, expressions
# Floats and Integers


# Integers are whole numbers, while floats can be whole
#	numbers or have fractional parts. CodeSkulptor treats
#	all numbers as floats unless otherwise stated.

print "Integers:", 5, 19, -2, 37
print "Floats:", -3.4, 5, 9.99999, 1/3
print

# There is a way to specifically convert a number from a 
#	float to an integer and vice versa.

# Float to Integer (int): truncates the decimal (leaves it off)
print "Ex. 1:", int(3)
print "Ex. 2:", int(7.4)
print "Ex. 3:", int(1.9)
print "Ex. 4:", int(-1.2)
print "Ex. 5:", int(-2.9)
print

# Integer to float: doesn't change anything
print "Ex. 6:", float(9)
print "Ex. 7:", float(-2)


print "--------"
# Python and CodeSkulptor cannot keep track of an infinite
#	number of decimal places.

print "Ex. 8:", .12345678901234567890


print "--------"
# Operations using floats and ints are not exact in python,
#	which leads to some interesting outputs

# These have different final digits and a different number
#	of digits as well
print "Ex. 9: ", 4 / 3
print "Ex. 10:", 25 / 3
print
print "Ex. 11:", 1 / 6
print "Ex. 12:", 13 / 6
print "Ex. 13:", 601 / 6
print

# In these ones, the output changes based on the grouping
#	of terms, even though they are mathematically equivalent
print "Ex. 14:", 5 * 4 / 3
print "Ex. 15:", 5 * (4 / 3)
print "Ex. 16:", 20 / 3
print

# Here is another weird one
print "Ex. 17:", 11.2 - 11

# Most programs don't require this level of precision, so 
#	you shouldn't have to worry about it too much in your
#	own coding.


