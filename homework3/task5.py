result = 0
q = False
while q is False:
    num = input('Введите числа через пробел, для завершения нажмите "q": ').split()
    for el in range(len(num)):
        if num[el] == 'q':
            q = True
            break
        else:
             result = result + int(num[el])
    print(result)
