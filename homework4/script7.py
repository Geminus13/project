def gen(num):
    f = 1
    for el in range(1, num+1):
        f *= el
        yield f

n = 10

for ind, el in enumerate(gen(n)):
    print(f'{ind+1}!: {el}')
