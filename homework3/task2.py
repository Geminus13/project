def data_user(name, second_name, date_birth, city, email, phone):
    print(f"Имя - {name}; Фамилия - {second_name}; Дата рождения - {date_birth}; Город - {city}; Email - {email}; Телефон - {phone}")

data_user(name = input('Введите имя: '),
    second_name = input('Введите фамилию: '),
    date_birth = input('Введите дату рождения: '),
    city = input('Введите город проживания: '),
    email = input('Введите электронную почту: '),
    phone = input('Введите номер телефона: '))
