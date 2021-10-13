num = input('Введите числа через пробел: ')
list = list(num.split())
i = 0
if len(list) > 1:
    while i < len(list) - 1:
        list[i], list[i+1] = list[i+1], list[i]
        i+=2
print(list)
