str = input('Введите слова через пробел: ')
result = str.split()
num = 1
for i in result:
    print(f'{num}.', i[0:10])
    num +=1
