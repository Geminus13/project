rating = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
i = 0
for el in rating:
    if num >= el:
        rating.insert(i, num)
        break
    i += 1
if num < el:
    rating.append(num)
print(rating)
