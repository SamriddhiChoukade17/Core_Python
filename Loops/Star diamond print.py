"""for i in range(1, 5):
    for j in range(1, i + 1):

        print(' ' * i)
        print('*' * j, end = " ")
    print()
"""

'''n = 4

for i in range(1, 10, 2):

    for k in range(n, 0, -1):
        print(end="\t")

    n = n - 1

    for j in range(1, i + 1):
        print("*", end="\t")

    print()
    print()'''

n = 5

for i in range(1, 11, 2):

    for j in range(n, 0, -1):
        print( end="\t")

    n = n -1

    for k in range(1, i+1):
        print("*", end="\t")

    print()
    print()

n = 1

for i in range(10, 0, -2):


    for j in range(n ,10 , 1):
        print(end="\t")

    n = n-1

    for k in range(10, i -1):
        print("*", end="\t")

    print()
    print()