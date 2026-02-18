import pickle
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, "\t", self.name, "\t", self.salary)

with open("D:/PycharmProjects/CorePython/Files/Employee", "wb") as file:
    emp = Employee(1, 'Raj', 50000)
    pickle.dump(emp, file)
