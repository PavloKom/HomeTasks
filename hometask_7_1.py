name = input("enter your name: ")
age = int(input("enter your age: "))


def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old."


print(say_hi(name, age))
