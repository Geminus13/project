import json

profit_list = []
profit_dict = {}
avprofit_dict = {}

with open('task7.txt') as file:
    for line in file:
        line = line.split()
        profit_dict[line[0]] = int(line[2]) - int(line[3])


        summ = 0
        i = 0
        for val in profit_dict.values():
            if val > 0:
                summ += val
                i += 1

        avprofit_dict['average_profit'] = summ/i

    profit_list.append(profit_dict)
    profit_list.append(avprofit_dict)

    print(profit_list)

with open("task7.json", "w") as file2:
    json.dump(profit_list, file2)
