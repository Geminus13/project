def my_func(x, y):
    return x**y

def my_func2(x, y):
    i = 0
    result = 1
    while y != i:
        result *= x
        i +=1
    return result

print(my_func(float(input('Введите x: ')), int(input('Введите y: '))))
print(my_func2(float(input('Введите x: ')), int(input('Введите y: '))))
