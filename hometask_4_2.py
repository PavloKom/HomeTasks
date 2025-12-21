numbers = [1, 0, 2, 0, 3, 4, 0, 3]

even_numbers = numbers[::2]
even_sum = sum(even_numbers)
result = even_sum * numbers[-1]

print(f'even numbers sum:', even_sum)
print(f'even numbers multiplied on last number:', result)
