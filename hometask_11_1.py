def prime_generator(n):
    for num in range(2, n + 1):
        prime = True
        for x in range(2, int(num / 2) + 1):
            if num % x == 0:
                prime = False
                break
        if prime:
            yield num


assert list(prime_generator(50)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

print(list(prime_generator(50)))
