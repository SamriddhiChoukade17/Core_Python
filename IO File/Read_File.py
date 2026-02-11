def readfile():
    file = open("D:/PycharmProjects/CorePython/Files/Hi_File", 'r')

    text = file.read()
    print(text)
    file.close()

readfile()