a = 10
b = 3

try:
    c = a/b
    print("division:", c)

except ZeroDivisionError as e:
    print("exception:", e)

else:
    print("this is else block")

finally:
    print("I am finally block")