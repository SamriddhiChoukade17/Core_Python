from typing import List

class Shape():
    def area(self):
        print("Shape Area")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self. width = width

    def area(self):
        rectangle_area = self.length * self.width
        print("rectangle Area: ", rectangle_area)
        return rectangle_area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = self.radius * self.radius
        print("Circle Area: ", circle_area)
        return circle_area

apple: List[Shape] = [Rectangle(10,15), Circle(6)]

for shape in apple:
    shape.area()