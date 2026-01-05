def common_elements():
    multiples_3 = [x for x in range(100) if x % 3 == 0]
    multiples_5 = [y for y in range(100) if y % 5 == 0]

    return set(multiples_3) & set(multiples_5)


print(common_elements())
