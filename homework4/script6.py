from itertools import count, cycle

my_counter = []
for el in count(3):
    if el == 11:
        break
    else:
        my_counter.append(el)
print(my_counter)

my_cycle = []
с = 0
for el in cycle([1, 2, 3]):
    if с > 11:
        break
    my_cycle.append(el)
    с += 1
print(my_cycle)
