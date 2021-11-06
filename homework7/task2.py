from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    @property
    def expense(self):
        return self.parametr / 6.5 + 0.5

class Suit(Clothes):
    @property
    def expense(self):
        return 2 * self.parametr + 0.3

    def sum_expense(self, list_suit):
        i = 0
        for suit in list_suit:
            i += suit.expense
        return f'Общий расход ткани на костюмы: {i}'


my_coat = Coat(10)
print(my_coat.expense)

my_suit1 = Suit(5)
print(my_suit1.expense)
my_suit2 = Suit(6)
my_suit3 = Suit(15)

list_suit = [my_suit1, my_suit2, my_suit3]

print(my_suit1.sum_expense(list_suit))
