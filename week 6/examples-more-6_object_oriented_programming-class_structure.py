# Object Oriented Programming
# Class Structure


# Classes

# Classes are defined using the word 'class' instead of 'def'.
#	By convention, their names are in camel case, which means
#	that there are no spaces or underlines, and the first
#	letter of each word is capitalized.

class ClassOne:
    def __init__(self):
        print "You made a ClassOne object!"
 
print "Ex. ClassOne:"
print
c = ClassOne()
# Printing a class lets you know what type of object it is.
print c
print
    
    
# Classes can contain methods. Methods are just functions 
#	inside of a class. They may or may not contain return
#	and/or print statements. The first parameter of every
#	method is the variable 'self', which refers to the 
#	object that is calling the class.

class ClassTwo:
    # This is the special method that initializes the object
    #	that is being created.
    def __init__(self):
        print "HI"
        
    # This method runs whenever an object is printed.
    def __str__(self):
        return "Hello"
        
    def another_method(self):
        print "Good job!"
        
    def adding_method(self, a, b):
        return a + b
    
print "Ex. ClassTwo"
print
c = ClassTwo()
# Notice that when you call methods, you don't explicitly
#	give them the parameter 'self'. 'self' is passed in 
#	by the program as the object calling the method, which
#	in this case is c.
c.another_method()
print c.adding_method(1, 2)
# Here the __str__ method is called by the program.
print c
print
    
# Classes can be used to keep track of variables and perform
#	operations on them. The values of the class' variables
#	are known as its state. To tell the class to keep track
#	of a variable, the first parameter, self, is used. Global
#	statements are not needed to change class variables.
    
class ClassThree:
    # Class variables should be defined and initialized inside
    #	this method.
    def __init__(self, start):
        self.number = start
        
    def __str__(self):
        return str(self.number)
        
    def increment(self):
        # self.number is not a global variable, so there is
        #	no global declaration.
        self.number += 1
        
    def get_number(self):
        return self.number
    
    def set_number(self, n):
        self.number = n

print "Ex. ClassTwo:"
print
c = ClassThree(3)
print c.get_number()
c.increment()
c.increment()
print c.get_number()
c.set_number(8)
print c.get_number()
print c
print
        
      
# Classes can also call other methods of the same class.

class ClassFour:
    def __init__(self):
        self.num = 5
     
    def __str__(self):
        return str(self.num)
        
    def add_num(self, n):
        self.num += n
        
    def print_num(self, w):
        print w, self.num
        
    # The parameters for both methods are required.
    def two_in_one(self, w, n):
        # self is used to call the other methods
        self.add_num(n)
        self.print_num(w)
        
c = ClassFour()
c.add_num(2)
c.print_num("One:")
c.two_in_one("Two:", 4)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
