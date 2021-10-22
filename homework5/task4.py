new_file = []
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open('task4-1.txt') as file:
    for line in file:
        line = line.split(' ', 1)
        new_file.append(rus[line[0]] + ' ' + line[1])

with open('task4-2.txt', 'w') as file2:
    file2.writelines(new_file)
