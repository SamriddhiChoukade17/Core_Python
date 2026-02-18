import pickle

from WriteObjectFile import employee
with open("D:\PycharmProjects\CorePython\Files\Employee", "rb") as file:

    obj = pickle.load(file)

    print("Printing employee information after unpickling")
    obj.display