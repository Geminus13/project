class Complex_num:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'z1 + z2 = {self.a + other.a}+{self.b + other.b}i'

    def __mul__(self, other):
        return f'z1 * z2 = {self.a * other.a - self.b * other.b}+{self.b * other.a + self.a * other.b}i'

    def __str__(self):
        return f'z = {self.a}+{self.b}i'

z1 = Complex_num(6, 5)
z2 = Complex_num(4, 2)

print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
