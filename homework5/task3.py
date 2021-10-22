with open('task3.txt') as file:
    min_oklad = []
    oklad = []
    for line in file:
        i = line.split()
        oklad.append(i[1])

        if int(i[1]) < 20000:
            min_oklad.append(i[0])

    av_oklad = 0
    for el in oklad:
        av_oklad = av_oklad + int(el)
    av_oklad = av_oklad/len(oklad)

print(f'Оклад менее 20к: {min_oklad}')
print(f'Средний оклад: {av_oklad}')
