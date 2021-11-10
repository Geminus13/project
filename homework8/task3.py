class MyException(Exception):
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
                    raise MyException(f"'{user_input}' неправильный формат")
                my_list.append(int(user_input))
            except MyException as e:
                print(e)
        return my_list

exp = MyException('start')
print(exp.check)
