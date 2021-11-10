class MyExeption(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise MyExeption('Делить на ноль нельзя!')
    c = a / b
    print(c)
except MyExeption as e:
    print('Наша ошибка')
    print(e)
except Exception:
    print('Другая ошибка')
