number = int(input('Введите целое положительно число: '))
i = 0
while number >= 1:
    mx = number % 10
    if mx >= i:
        i = mx
    number //= 10
print(i)
