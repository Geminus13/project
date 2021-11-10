class MyExeption(Exception):
    def __init__(self, text):
        self.text = text

    @property
    def check(self):
        my_list = []
        while True:
            user_input = input("Введите число для заполнения списка или 'stop' для выхода: ")

            if user_input == "stop":
                break

            try:
                if not user_input.isdigit():
                    raise MyExeption(f"'{user_input}' неправильный формат")
                my_list.append(int(user_input))
            except MyExeption as e:
                print(e)
        return my_list

exp = MyExeption('start')
print(exp.check)
