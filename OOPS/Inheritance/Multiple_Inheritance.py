class Addition:
    def sum(self, x, y):
        return x + y;

class Multiplication:
    def product(self, x, y):
        return x * y;

class Division(Addition, Multiplication):
    def division(self, x, y):
        return x / y;

divided_obj = Division()
print(divided_obj.sum(5, 2))
print(divided_obj.product(10,5))
print(divided_obj.division(40,5))
