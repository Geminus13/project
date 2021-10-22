import codecs

lessons = {}
with codecs.open('task6.txt',"r", "utf-8" ) as file:
    for line in file:
        numbers = []
        line = line.split()

        for el in line:
            el = el.split('(')
            i = 0

            if el[i].isdigit():
                numbers.append(int(el[i]))
            i += 1
        lessons[line[0]] = sum(numbers)
print(lessons)
