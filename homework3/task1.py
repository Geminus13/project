def div_func():
    num1 = float(input('Введите делимое: '))
    num2 = float(input('Введите делитель: '))
    if num2 != 0:
        result = num1/num2
    else:
        return 'Attention! На ноль делить нельзя!'
    return result

print(div_func())
