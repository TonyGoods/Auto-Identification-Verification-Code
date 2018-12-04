def saveValue(w1, w2, w3):
    file = open('value.txt', 'w+')
    file.write('w1:\n')
    for i in range(len(w1)):
        for j in range(len(w1[i])):
            file.write(str(w1[i][j]) + '\n')
        file.write('wrap\n')
    file.write('w2:\n')
    for i in range(len(w2)):
        for j in range(len(w2[i])):
            file.write(str(w2[i][j]) + '\n')
        file.write('wrap\n')
    file.write('w3:\n')
    for i in range(len(w3)):
        for j in range(len(w3[i])):
            file.write(str(w3[i][j]) + '\n')
        file.write('wrap\n')
    print('save successful')


def getValue():
    file = open('value.txt', 'r')
    line = file.readline()
    w1 = [[]]
    i = 0
    while line:
        line = file.readline()
        if line == 'w2:\n':
            w1.pop()
            i = 0
            break
        if line == 'wrap\n':
            w1.append([])
            i += 1
            continue
        w1[i].append(float(line))
    w2 = [[]]
    while line:
        line = file.readline()
        if line == 'w3:\n':
            w2.pop()
            i = 0
            break
        if line == 'wrap\n':
            i += 1
            w2.append([])
            continue
        w2[i].append(float(line))

    w3 = [[]]
    while line:
        line = file.readline()
        if line == 'wrap\n':
            w3.append([])
            i += 1
            continue
        if line == '':
            w3.pop()
            break
        w3[i].append(float(line))
    print(len(w2))
    return w1, w2, w3
