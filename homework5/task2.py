with open('task2.txt') as file:
    lines = len(file.readlines())

    print("Lines:", lines)
    file.seek(0)

    words = 0
    i = 1
    for word in file.readlines():
        words += len(word.split())
        print(f'{i} line: {len(word.split())} words')
        i += 1

    print("All words:", words)
