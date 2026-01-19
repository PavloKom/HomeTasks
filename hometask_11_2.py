from inspect import isgenerator

def generate_cube_numbers(end):
    num = 2
    while True:
        cube = num ** 3
        if cube >= end:
            break
        yield cube
        num += 1


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
print("ok")
print(list(generate_cube_numbers(1000)))

