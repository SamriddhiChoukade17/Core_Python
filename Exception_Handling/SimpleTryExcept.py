try:
    a = 15
    b = 2
    c = a/b
    print("a/b : ", c)
except ZeroDivisionError as e:
    print("can't divide by zero : ", e)
else:
    print("Hi I'm Else block")
finally:
    print("Hi I'm Finally")