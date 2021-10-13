prod = []
num = 1
stop = ''
while stop != 'нет':
    name = input('Введите название товара: ')
    price = input('Введите цену: ')
    count = input('Введите кол-во на складе: ')
    unit = input('Введите единицу измерения: ')
    prod.append((num, {'название' : name, 'цена' : price, 'кол-во' : count, 'ед' : unit}))
    num += 1
    stop = input('Хотите продолжить заполнение? (да/нет): ')

result = {}
for num, dict in prod:
    for key, value in dict.items():
        if not result.get(key):
            result[key] = [value]
        else:
            result[key].append(value)

for key, value in result.items():
    result[key] = list(set(value))

print(result)
