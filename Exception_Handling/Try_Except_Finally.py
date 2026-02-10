a = 10
b = 0

try:
    c = a/b
    print("division:", c)

except ZeroDivisionError as e:
    print("exception:", e)

finally:
    print("Hi I'm finally block")