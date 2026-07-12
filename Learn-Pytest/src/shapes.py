import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError("Radius must be >= 0")

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        if length >= 0 and breadth >= 0:
            self.length = length
            self.breadth = breadth
        else:
            raise ValueError("Dimensions must be >=0")

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        else:
            return self.length == other.length and self.breadth == other.breadth

    def area(self):
        return self.breadth * self.length

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(length=side_length, breadth=side_length)
