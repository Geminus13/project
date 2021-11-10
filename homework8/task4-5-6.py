class MyException(Exception):
    def __init__(self, text):
        self.text = text


class Store:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_store(self, techn):
        self.lists.update({techn.serial_number : [techn.title, techn.amount]})
        print(f'На склад {self.title} получено оборудование: {techn.title}, серийный номер - {techn.serial_number}, кол-во - {techn.amount} шт.')


    def give_to_store(self, techn, other):
        give_amount = input('Введите кол-во единиц оборудования для передачи: ')
        try:
            if not give_amount.isdigit():
                raise MyException(f"'{give_amount}' неправильный формат")
            give_amount = int(give_amount)
        except MyException as e:
            print(e)
            return give_amount
        self.give_lists.update({techn.serial_number : [techn.title, give_amount, other.title]})
        print(f'Передано оборудование на склад {other.title}: {techn.title}, серийный номер {techn.serial_number}, кол-во - {give_amount} шт.')
        other.lists.update({techn.serial_number : [techn.title, give_amount]})
        self.lists.update({techn.serial_number : [techn.title, techn.amount - give_amount]})
        if techn.amount - give_amount == 0:
            self.lists.pop(techn.serial_number)


    @property
    def list_techn(self):
        return f'Текущее оборудование на складе {self.title}: {self.lists}'


class Tech:
    def __init__(self, title, serial_number, amount):
        self.title = title
        self.serial_number = serial_number
        self.amount = amount


    def __str__(self):
        return str(self.title)

class Printer(Tech):
    def __init__(self, title, serial_number, amount, print_feature):
        Tech.__init__(self, title, serial_number, amount)
        self.print_feature = print_feature


class Scanner(Tech):
    def __init__(self, title, serial_number, amount, scan_feature):
        Tech.__init__(self, title, serial_number, amount)
        self.scan_feature = scan_feature

class Xerox(Tech):
    def __init__(self, title, serial_number, amount, copy_feature):
        Tech.__init__(self, title, serial_number, amount)
        self.copy_feature = copy_feature


store1 = Store('№1')
store2 = Store('№2')
a = Printer('HP', 6598745, 2, 100)
b = Scanner('Epson', 9854777, 1, 6000)
c = Xerox('Brother', 9562133, 1, 35)


print(a)
print(b)
print(c)

store1.take_to_store(a)
store1.take_to_store(b)
store1.take_to_store(c)
print(store1.list_techn)
print(store2.list_techn)

store1.give_to_store(a, store2)

print(store1.list_techn)
print(store2.list_techn)
