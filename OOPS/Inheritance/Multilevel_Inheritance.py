class Student:
    def getStudent(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.gender = input("Enter your gender: ")


class Test(Student):
    def getMarks(self):
        self.studentClass = input("Enter your class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.hindi = int(input("Hindi: "))
        self.history = int(input("History: "))


class Marks(Test):
    def display(self):
        print("\n\nName: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        total_marks = self.literature + self.math + self.history + self.hindi
        print("Total marks: ", total_marks)


m = Marks()
m.getStudent()
m.getMarks()
m.display()