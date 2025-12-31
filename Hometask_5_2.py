while True:
    first_number = float(input("Enter first number: "))
    operation = input("Enter operation: +, -, *, / : ")
    second_number = float(input("Enter second number: "))

    if operation == "+":
        print("Result:", first_number + second_number)
    elif operation == "-":
        print("Result:", first_number - second_number)
    elif operation == "*":
        print("Result:", first_number * second_number)
    elif operation == "/":
        if second_number != 0:
            print("Result:", first_number / second_number)
    else:
        print("Error: division by zero")
    answer = input("Continue? (y/n): ").lower()
    if answer == "y":
        continue
    elif answer == "n":
        break