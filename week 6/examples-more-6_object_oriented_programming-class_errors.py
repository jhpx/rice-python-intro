# Object Oriented Programming
# Class Errors


# Here are some errors to look out for while using classes.

# Classes are created using the keyword 'class', not 'def',
#	although they still require the ':' at the end of the 
#	line.

#def ClassOne:
#    def __init__(self):
#        print "You created a ClassOne object."
   
#class X
#    def __init__(self):
#        pass
    
class ClassOne:
    def __init__(self):
        print "You created a ClassOne object."
        
    def p(self):
        print "HI"

print "Ex. 1 (ClassOne):"
c = ClassOne()
c.p()
print


# Instantiating an object of a class is done using the class
#	name and parenthesis only.

print "Ex. 2 (ClassOne):"
c = ClassOne()

#c = new ClassOne()
#c = ClassOne.__init__()
#c = ClassOne.__init__(self)

# Don't forget the parenthesis
c = ClassOne
print "Error:", c
#c.p()
print


# Class and method names must follow the same rules that
#	variable names do.

#class print:   
#class so-this:
#class _9
#class 4th:

class Test:
    def __init__(self):
        pass
    
#    def print(self):
#        print "HI"

#    def a&b(self):
#        print "A"
   
    
# Self always needs to be the first parameter in any method.
#	Uncomment the methods to see the error messages.
        
class Example1:
    def __init__():
        print "HI"
        
#e = Example1()
    
class Example2:
    def __init__(self):
        pass
        
    def add(a, b):
        return a + b
    
    def correct_add(self, a, b):
        return a + b
    
print "Ex. 3 (Example2):"
e = Example2()
#print e.add(4, 5)
# In the next call, the Example object e is being added to 
#	the number 5, which causes the error.
#print e.add(5)
print "Correct Addition:", e.correct_add(4, 5)
print


# Self also does not need to be passed as a parameter when
#	calling methods.

class Example3:
    def __init__(self):
        pass
    
    def f(self):
        print "HI"
        
print "Ex. 4 (Example3):"
e = Example3()
#e.f(self)
#e.f(e)
e.f()
print
        
        
# Forgetting to use 'self' when referencing class variables
#	causes issues similar to forgetting the 'global'
#	statement in functions.
     
class Example4:
    def __init__(self, n):
        num = n
        
    def get_num1(self):
        return num
    
    def get_num2(self):
        return self.num
    
c = Example4(5)
#print c.get_num1()
#print c.get_num2()
    
class Example5:
    def __init__(self, num):
        self.num = num
        
    def get_num(self):
        return num
    
    def actual_get_num(self):
        return self.num
    
    def set_num(self, new):
        num = new
        
    def actual_set_num(self, new):
        self.num = new
  
print "Ex. 5 (Example5):"
e = Example5(3)
#print e.get_num()
print "E num:", e.actual_get_num()
e.set_num(5)
print "Nothing Changed:", e.actual_get_num()
e.actual_set_num(5)
print "Now it did:", e.actual_get_num()
print

# However, using self.something outside of a class doesn't 
#	work.

#print self.num
#print self.get_num()

# To call methods of a class, an object of the class needs
#	to be used.

print "Ex. 6 (Example5):"
#print actual_get_num()
print e.actual_get_num()
#print actual_get_num(e)
print

# You also need to remember the parenthesis

print "Ex. 7 (Example6):"
print "Here it is:"
x = e.actual_get_num
#print x + 2
print e.actual_get_num
print
    
    
print "------------------------"
print
    
# Methods follow the same rules as functions, but the indentation
#	is different.

class B:
    # Forgot the 'def'
#    __init__(self):
#        print "HI"
   
    # Bad indentation
#def __init__(self):
#    print "HI"

    # Missing ':'
#    def __init__(self)
#        print "HI"
        
    # Missing (self)
#    def __init__:
#        print "HI"
     pass
 
    
# Be careful not to give multiple methods the same name.

class C:
    def __init__(self):
        self.num1 = 0
        self.num2 = 2
        
    def get_num(self):
        return self.num1
      
    def get_num(self):
        return self.num2

print "Ex. 8 (C):"
c = C()
print c.get_num()
print c.get_num()
print
        
        
# You can reference global variables inside of your class, 
#	but you need to declare them as such if you plan on
#	modifying them.

my_num = 7

class D:
    def __init__(self):
        self.num = my_num
        
    def add_num(self):
        self.num += 1
    
    def print_num(self):
        print self.num
        
    def bad_add_global(self):
        my_num += 1
        
    def add_global(self, n):
        n += 1
        print "add_global:", n
        
    def good_add_global(self):
        global my_num
        my_num += 1
   
print "Ex. 9 (D):"        
c = D()
c.print_num()
c.add_num()
c.print_num()
print "1:", my_num
#c.bad_add_global()
c.add_global(my_num)
print "2:", my_num
c.good_add_global()
print "3:", my_num
print
        

# When calling one method of a class from a different method
#	of the class, other issues can occur.

class E:
    def __init__(self):
        self.num = 2
    
    def add_num(self, n):
        self.num += n
        
    def print_num(self):
        print self.num
        
    def print_and_add_num_1(self, n):
        self.add_num(n)
        self.print_num()
        
    def print_and_add_num_2(self, n):
        E.add_num(self, n)
        E.print_num(self)
    
    # Forgot to take all of the arguments for the methods
    #	it will be calling.
    def print_and_add_num_3(self):
        self.add_num()
        self.print_num()
    
    # Forgot to include self
    def print_and_add_num_4(self, n):
        add_num(n)
        print_num()
  
print "Ex. 10. (E):"
c = E()
c.print_num()
c.add_num(3)
c.print_num()
c.print_and_add_num_1(6)
c.print_and_add_num_2(-10)
#c.print_and_add_num_3()
#c.print_and_add_num_4(4)
    
    
# One last note: While the following is valid python, if you
#	have never used python or classes before, we highly 
#	recommend that you avoid using this type of variable.
#	They are not necessary for any of the work in this class.

class F:
    # While the following statements do not cause errors, you
    #	should avoid using them.
    num = 9
    my_variable = "HELLO"
    def __init__(self):
        pass
    
c = F()
    
    
    
    
        