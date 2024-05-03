class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

shape = Shape()
square = Square(7)
rectangle = Rectangle(7,8)

print("Area of the shape:", shape.area())  
print("Area of the square:", square.area())  
print("Area of the rectangle:", rectangle.area())
