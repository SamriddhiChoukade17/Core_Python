import os

s = open("D:/PycharmProjects/CorePython/Files/Keyboard")
position = s.seek(5)
str = s.read(4)
print(str)
print(s.tell())
