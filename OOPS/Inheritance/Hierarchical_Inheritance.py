class Shape:
    def __init__(self, color = '', borderWidth = 0):
        self.color = color
        self.borderWidth = borderWidth

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, bw):
        self.borderWidth = bw

    def getBorderWidth(self):
        return self.borderWidth

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0, color = '', borderWidth = 0):
        self.length = length
        self.width = width
        super().__init__(color, borderWidth)


    def setLength(self, l):
        self.length = 1

    def getLength(self):
        return self.length

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width


class Circle(Shape):
    def __init__(self, radius = 0, color = '', borderWidth = 0):
        self.radius = radius
        super().__init__(color, borderWidth)

    def setRadius(self, r):
        self.radius = r

    def getRadius(self):
        return self.radius


r = Rectangle(10, 30, "Pink", 100)
print("Rectangle: ")
print("Length: ", r.getLength())
print("Width: ", r.getWidth())
print("Color: ", r.getColor())
print("Border Width: ", r.getBorderWidth())

c = Circle(10, 'White', 5)
print("\nCircle:")
print("Radius:", c.getRadius())
print("Color:", c.getColor())
print("Border Width:", c.getBorderWidth())