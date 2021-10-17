from itertools import count, cycle

for el in count(3):
    if el == 11:
        break
    else:
        print(el)

с = 0
for el in cycle([1, 2, 3]):
    if с > 11:
        break
    print(el)
    с += 1
