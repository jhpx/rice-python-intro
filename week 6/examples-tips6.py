###################
# Broken code

class ball:
    def ball(pos, rad):
        position = pos
        radius = rad
        return ball
    
    def get_position():
        return position

b = ball([0,0], 10)

print get_position(b)



###################
# Fixed code

class Ball:
    def __init__(self, pos, rad):
        self.position = pos
        self.radius = rad
    
    def get_position(self):
        return self.position

b = Ball([0,0], 10)

print b.get_position()



##################
# Mutation with classes and objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, newx):
        self.x = newx
    
    def get_x(self):
        return self.x

p = Point(4,5)
q = Point(4,5)
r = p

p.set_x(10)

print p.get_x()
print q.get_x()
print r.get_x()


##################
# Example while

def countdown(n):
    """Print the values from n to 0."""

    i = n
    while i >= 0:
        print i
        i -= 1

countdown(5)


##################
# Collatz

def collatz(n):
    """Prints the values in the Collatz sequence for n."""

    i = n
    while i > 1:
        print i
        
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3*i +1
           
colnatz(1000)


#################
# Timeout

i = 1
while i > 0:
    i += 1
