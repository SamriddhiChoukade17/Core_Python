class Person:
    count = 0

    def __init__(self):
        self.name = ''
        self.address = ''
        Person.count += 1

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


p = Person()
p.set_name('abc')
print('Name:', p.get_name())
print("Person __doc__",p.__doc__)
print("Person Name",p.name)
print("Person __module__",p.__module__)
print("Person __dict__",p.__dict__)


print('Count:', Person.count)
print('Memory address of p:', id(p))
