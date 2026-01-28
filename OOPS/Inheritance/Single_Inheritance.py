class Shape:
    def __init__(self):
        set.color = ''
        set.borderWidth = 0

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, bw):
        self.borderWidth = bw

    def getBorderWidth(self):
        return self.borderWidth


class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def setLength(self, l):
        self.length = 1

    def getLength(self):
        return self.length

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width


r = Rectangle()
r.setLength(15)
r.setWidth(35)
r.setColor("green")
r.setBorderWidth(30)

print("Length: ", r.getLength())
print("Width: ", r.getWidth())
print("Color: ", r.getColor())
print("Border Width: ", r.getBorderWidth())
