F = [1, 1, 1, 1, 0, 0, 0, 1]


def createTruthTable(F):
    initialTable = [[0, 0, 0], 
                    [0, 0, 1],
                    [0, 1, 0],
                    [0, 1, 1],
                    [1, 0, 0],
                    [1, 0, 1],
                    [1, 1, 0],
                    [1, 1, 1]]
    

    for i in range(0, len(initialTable)):
        initialTable[i].append(F[i])

    return initialTable


def dualityFunction(F):
    print('Двоїста функція')
    F1 = F

    for i in range(len(F1)):
        if F1[i] == 0:
            F1[i] = 1
        else: 
            F1[i] = 0
    
    F2 = F1[::-1]
    print(F2)
    print()


def createDDNF(F):
    print ("Досконала диз'юнктивна нормальна форма")
    truthTable = createTruthTable(F)

    ddnf = 'f(x1, x2, x3) = '
    for i in range(len(truthTable)):
        if truthTable[i][3] == 1:
            ddnf += '('
            for j in range(len(truthTable[i]) - 1):
                if truthTable[i][j] == 1:
                    ddnf += ('x' + str(j+1))
                else:
                    ddnf += ('¬x' + str(j+1))

                if j+1 != 3:
                    ddnf += str(' ∧ ')

            ddnf += ') v '
    
    newDdnf = ddnf[:len(ddnf) - 3]

    print(newDdnf)
    print()


def createDKNF(F):
    print ("Досконала кон’юнктивна нормальна форма")
    truthTable = createTruthTable(F)

    dknf = 'f(x1, x2, x3) = '
    for i in range(len(truthTable)):
        if truthTable[i][3] == 0:
            dknf += '('
            for j in range(len(truthTable[i]) - 1):
                if truthTable[i][j] == 0:
                    dknf += ('x' + str(j+1))
                else:
                    dknf += ('¬x' + str(j+1))

                if j+1 != 3:
                    dknf += str(' v ')

            dknf += ') ∧ '
    
    newDknf = dknf[:len(dknf) - 3]

    print(newDknf)
    print()


def polynomCoefs():
    arr = [F]
    while len(arr[-1]) != 1:
        temp = []
        for i in range(len(arr[-1]) - 1):
            temp.append(arr[-1][i] ^ arr[-1][i + 1])
        arr.append(temp)
    a = []
    for i in arr:
        a.append(i[0])
    return a


def polynom():
    coefs = polynomCoefs()
    
    table = createTruthTable(F)
    polynom = 'f(x1, x2, x3) ='
    arr = []
    if coefs[0] == 1:
        arr.append('1')
    for i in range(1, len(coefs)):
        if coefs[i] == 1:
            temp = ''
            for j in range(3):
                if table[i][j] == 1:
                    temp += 'x' + str(j +1)
            arr.append(temp)

    print(polynom + ' + '.join(arr))
    print()


def checkConstants(F):
    if F[0] == 0:
        print('Функція збергігає константу 0')
    else:
        print('Функція не збергігає константу 0')

    print()

    if F[7] == 1:
        print('Функція збергігає константу 1')
    else:
        print('Функція не збергігає константу 1')

    print()


def selfDualFunction(F):

    F1 = F

    for i in range(len(F1)):
        if F1[i] == 0:
            F1[i] = 1
        else: 
            F1[i] = 0
    
    F2 = F1[::-1]

    if F2 == F:
        print('Функція самодвоїста')
    if F2 != F:
        print('Функція не самодвоїста')
    
    print()


def monotonicFunction():
    initialTable = [[0, 0, 0], 
                    [0, 0, 1],
                    [0, 1, 0],
                    [0, 1, 1],
                    [1, 0, 0],
                    [1, 0, 1],
                    [1, 1, 0],
                    [1, 1, 1]]

    count = 0

    isMonotonic = True

    for i in range (len(initialTable)):
        for j in range(len(initialTable)):
            for k in range(len(initialTable[i])):
                if initialTable[i][k] >= initialTable[j][k]:
                    count += 1
            if ((count == 3) and (F[i] < F[j])):
                isMonotonic = False

            count = 0

    if isMonotonic == True:
        print('Функція монотонна')
    else:
        print('Функція не монотонна')

    print()


initialTable = createTruthTable(F)

print('   X', 'Y', 'Z', 'F', sep = '      ')
print(' --------------------------')
for i in range(len(initialTable)):
    for j in range(len(initialTable[i])):
        print(' |', initialTable[i][j], end = ' | ', )
    print('\n','--------------------------')
    print()


dualityFunction(F)

createDDNF(F)

createDKNF(F)

polynomCoefs()

polynom()

checkConstants(F)

selfDualFunction(F)

monotonicFunction()

polynomCoefs = polynomCoefs()

print('Функція лінійна: ' + str(
    polynomCoefs[3] == 0 and polynomCoefs[5] == 0 and polynomCoefs[6] == 0 and polynomCoefs[7] == 0))
