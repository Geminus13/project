class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

person = Position('Иван', 'Иванов', 'менеджер', 25000, 5000)
print(person.get_full_name(), person.get_total_income())
print(person.name)
