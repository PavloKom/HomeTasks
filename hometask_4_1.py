numbers = [1, 0, 2, 0, 3, 4, 0]

zero = 0
n = len(numbers)

while zero < n:
    if numbers[zero] == 0:
        numbers.pop(zero)
        numbers.append(0)
        n -= 1
    else:
        zero += 1
print(numbers)
