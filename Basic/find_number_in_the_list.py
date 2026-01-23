list = [12, 15, 42, 63, 17, 11, 19, 20]
number = 85
count = 0

for i in list:
    if i == number:
        count += 1

if count > 0:
    print("number is present in the list: ", number)
else:
    print("number is not present in the list")
