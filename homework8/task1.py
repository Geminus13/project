class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split('-'):
            my_date.append(int(i))
        return my_date

    @staticmethod
    def valid(my_date):

        if 1 <= my_date[0] <= 31:
            if 1 <= my_date[1] <= 12:
                if 2021 >= my_date[2] >= 0:
                    return f'OK'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата\n День: {Data.extract(self.day_month_year)[0]}\n Месяц: {Data.extract(self.day_month_year)[1]}\n Год: {Data.extract(self.day_month_year)[2]}'

d = Data('10-11-2021')
print(d)

d2 = [10, 11, 2021]
print(Data.valid(d2))
d3 = [87, 11, 2021]
print(Data.valid(d3))
d4 = [10, 13, 2021]
print(Data.valid(d4))
d5 = [10, 11, 2023]
print(Data.valid(d5))
