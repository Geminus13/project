with open("text.txt", 'a+') as file:
    content = input('Введите строку: ')
    file.write(content)
    while content != '':
        content = input('Введите строку: ')
        file.write(content)
    file.seek(0)
    print(file.read())
