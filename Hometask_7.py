first_number =int(input("Enter a 4-digit number: "))

print(int((first_number % 10000 - first_number % 1000) / 1000))
print(int((first_number % 1000 - first_number % 100) / 100))
print(int((first_number % 100 - first_number % 10) / 10))
print(first_number % 10)
