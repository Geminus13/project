with open('task5.txt', 'w') as file:
    line = input('Введите числа через пробел: ')
    file.write(line)

    summ = 0
    for el in line.split():
      summ = summ + int(el)

print(f'Сумма чисел: {summ}')
