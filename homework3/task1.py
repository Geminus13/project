def div_func(num1, num2):
    if num2 != 0:
        result = num1/num2
    else:
        return 'Attention! На ноль делить нельзя!'
    return result

print(div_func(float(input('Введите делимое: ')), float(input('Введите делитель: '))))
