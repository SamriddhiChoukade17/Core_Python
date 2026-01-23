str = "vivek singh rajput"
str_list = str.split()

for str in str_list:
    reversed_str = " "
    for char in str:
        reversed_str += char
    print(reversed_str, end = "")