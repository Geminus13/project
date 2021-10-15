def my_func(arg1, arg2, arg3):
    max_num = max(arg1, arg2, arg3)
    max_num2 = max(min(arg1, arg2), min(arg2, arg3), min(arg1, arg3))
    result = max_num + max_num2
    return result

print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))
