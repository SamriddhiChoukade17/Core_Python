n = 4

for i in range(1, 10, 2):

    for j in range(n, 0, -1):
        print(end="\t")

    n = n - 1

    for k in range(1, i + 1):
        print("*", end="\t")

    print()
    print()

n = 1

for i in range(7, 0, -2):
    for j in range(1, n + 1):
        print(end="\t")
    n = n + 1

    for k in range(i, 0, -1):
        print("*", end="\t")

    print()
    print() 
