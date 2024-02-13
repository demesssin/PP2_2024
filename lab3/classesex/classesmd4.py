import math

class Point:
    def __init__(self, x = int(input()), y = int(input())):
        self.x = x
        self.y = y
    def show(self):
        return "Points: ({}, {})".format(self.x, self.y)
    
    def move(self, ax = int(input()), ay = int(input())):
        self.x += ax
        self.y += ay
        return "Moved coordinates:{}, {}".format(self.x, self.y)
    
    def dist(self, secondx = int(input()), secondy = int(input())):
        distx = self.x - secondx
        disty = self.y - secondy
        return math.sqrt(distx**2 + disty**2)

p = Point()
s = p.show()
print(s)
q = p.move()
print(q)
m = p.dist()
print(m)
