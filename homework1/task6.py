a = int(input('Введите количество км в 1-ый день: '))
b = int(input('Введите количество км в последний день: '))
day = 1
print(f'{day}-й день: ', '{:.2f}'.format(a))
if a > 0:
    while a <= b:
        a = a * 1.1
        day += 1
        print(f'{day}-й день: ', '{:.2f}'.format(a))
else:
    print('Количество км меньше или равно 0, введите другое число!')
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
