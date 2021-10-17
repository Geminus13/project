from functools import reduce

items = [el for el in range(100, 1001) if el % 2 == 0]
mul_all = reduce(lambda x, y: x * y, items)

print(mul_all)
