def my_func(x, y):
    return 1/x ** abs(y)

def my_func2(x, y):
    i = 0
    result = 1
    y = abs(y)
    while y != i:
        result *= 1/x
        i +=1
    return result

print(my_func(float(input('Введите положительное "x": ')), int(input('Введите отрицательное "y": '))))
print(my_func2(float(input('Введите положительное "x": ')), int(input('Введите отрицательное "y": '))))
