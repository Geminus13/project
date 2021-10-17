from itertools import count

def gen():
    f = 1
    for el in count(1):
        f *= el
        yield f

g = gen()

i = 0
for el in g:
    if i < 10:
        print(el)
        i += 1
    else:
        break
