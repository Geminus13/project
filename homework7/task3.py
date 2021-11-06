class Cell:
    def __init__(self, cell):
        self.cell = int(cell)
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')


    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell) if self.cell - other.cell >= 0 else 'Отрицательно число!'

    def __mul__(self, other):
        return Cell(abs(self.cell * other.cell))

    def __truediv__(self, other):
        return Cell(round(self.cell // other.cell))

    def make_order(self, count):
        x = ''
        for i in range(int(self.cell/count)):
            x += f'{self.simbol * count}\\n'
        x += f'{self.simbol * (self.cell % count)}'
        return x

my_cell = Cell(15)
print(my_cell)

my_cell2 = Cell(10)
print(my_cell + my_cell2)
print(my_cell - my_cell2)
print(my_cell2 - my_cell)
print(my_cell * my_cell2)
print(my_cell / my_cell2)

print(my_cell.make_order(5))
