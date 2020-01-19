class Quadrangle(object):
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

    def getArea(self):
        print((self.first * self.second * self.third * self.fourth) / 2, " is the area of Quadrangle")


class Rectangle(Quadrangle):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
        
    def getArea(self):
        print(self.length * self.breath, " is area of Rectangle")
        

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
    
    def getArea(self):
        print(self.side * self.side, " is area of Square")
        
quad = Quadrangle(10, 20, 30, 40)
quad.getArea()

rect = Rectangle(10, 20)
rect.getArea()

squr = Square(10)
squr.getArea()