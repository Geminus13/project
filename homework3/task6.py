def int_func(str):
    return str[0].upper() + str[1:].lower()


str_user = input('Введите слова через пробел: ').split()
result = ''
for el in str_user:
    el = int_func(el)
    result = result + ' ' + el
result = result[1:]
print(result)
