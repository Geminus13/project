def data_user(name, second_name, date_birth, city, email, phone):
    print(f"Имя - {name}; Фамилия - {second_name}; Дата рождения - {date_birth}; Город - {city}; Email - {email}; Телефон - {phone}")

data_user(name = input('Введите имя: '),
    second_name = input('Введите фамилию: '),
    date_birth = input('Введите дату рождения "day.month.year": '),
    city = input('Введите город проживания: '),
    email = input('Введите электронную почту: '),
    phone = input('Введите номер телефона: '))

data_user(name = 'Настя',
    second_name = 'Иванова',
    date_birth = '30.06.1993',
    city = 'Краснодар',
    email = 'test@mail.ru',
    phone = '89112223344')
