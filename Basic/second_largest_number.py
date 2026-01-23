number = [25, 52, 46, 81, 954, 62, 3479, 564]
largest = 0
second_largest = 0

for num in number:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("the largest number is", largest)
print("the second largest number is", second_largest)
