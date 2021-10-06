income = int(input('Введите выручку: '))
outplay = int(input('Введите издержки: '))
if income > outplay:
    profit = income - outplay
    print('Прибыль:', profit)
    eff = profit/income*100
    print('Рентабельность составляет: ', eff,'%')
    worker = int(input('Введите количество сотрудников: '))
    print('Прибыль в расчете на одного сотрудника: ', profit/worker)
else:
    loss = income - outplay
    print('Денег нет, но вы держитесь! Баланс: ', loss)
