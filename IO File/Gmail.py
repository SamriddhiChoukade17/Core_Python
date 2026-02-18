import re

def readLine():
    file = open("D:/PycharmProjects/CorePython/Files/Keyboard", 'r')    #open a file
    file1 = open("D:/PycharmProjects/CorePython/Files/Selected_Gmail.txt", 'w')
    for line in file:
        if (re.search("@gmail.com", line)):
            file1.write(line)
    file.close()
    file1.close()

readLine()