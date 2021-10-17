from sys import argv

def salary(h, r, p):
    h = float(h)
    r = float(r)
    p = float(p)
    return h * r + p

print(f'Выработка в часах: {argv[1]}; Ставка в час: {argv[2]}; Премия: {argv[3]}')
print('Заработная плата: ', salary(h=argv[1], r=argv[2], p=argv[3]))
