month = input('Введите число месяца: ')
win = 'зима'
sum = 'лето'
aut = 'осень'
spr = 'весна'
season_dict = {'1' : win, '2' : win, '3' : spr, '4' : spr, '5' : spr, '6' : sum, '7' : sum, '8' : sum, '9' : aut, '10' : aut, '11' : aut, '12' : win}
print(season_dict[month])

season_list = [win, win, spr, spr, spr, sum, sum, sum, aut, aut, aut, win]
print(season_list[int(month)-1])
