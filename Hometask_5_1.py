import keyword
import string

var_name = (input("Enter a string: "))

valid_name = True
underscore_count = 0

if var_name[0].isdigit():
    valid_name = False
elif var_name in keyword.kwlist:
    valid_name = False
elif var_name == " ":
    valid_name = False

for char in var_name:
    if char.isupper():
        valid_name = False
    elif char in string.punctuation and char == " " and char != "_":
        valid_name = False
    elif char == "_":
        underscore_count += 1
        if underscore_count > 1:
            valid_name = False

print(valid_name)
