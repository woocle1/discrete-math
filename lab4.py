import numpy as np
m = [[1, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 0], [0, 1, 1, 1, 1]]


print('Завдання 1')
def checkReflective(m):
    reflective = True
    for i in range(len(m)):
        for j in range(len(m)):
            if (i == j):
                if (m[i][j] != 1):
                    reflective = False
                    return reflective

    return reflective

resultReflective = checkReflective(m)


def checkSemmetric(m):
    symmetric = True
    for i in range(len(m)):
        for j in range(len(m)):
            if ((m[i][j] != m[j][i])  & (i != j)):
                symmetric = False
                return symmetric

    return symmetric

resultSymmetric = checkSemmetric(m)


def checkTransitivity(m):
    transitivity = True
    for a in range (len(m)):
        for b in range (len(m)):
            for c in range (len(m)):
                if ((m[a][b] == 1) & (m[b][c] == 1)):
                    if (not (m[a][c] == 1)):
                        transitivity = False
                        return transitivity

    return transitivity

resultTransitivity = checkTransitivity(m)


def checkAntisymmetric(m):
    antisymmetric = True
    for i in range(len(m)):
        for j in range(len(m)):
            if ((m[i][j] == 1) & (m[j][i] != 0) & (i != j)):
                antisymmetric = False
                return antisymmetric
            
    return antisymmetric

resultAntisymmetric = checkAntisymmetric(m)


def checkAsymmetric(m):
    asymmetric = True
    for i in range(len(m)):
        for j in range(len(m)):
            if ((m[i][j] == 1) & (m[j][i] != 0)):
                asymmetric = False
                return asymmetric
    
    return asymmetric

resultAsymmetric = checkAsymmetric(m)


def checkEquivalence():
    equivalence = 0
    for i in range(1):
        if (resultReflective == True):
            equivalence += 1
        if (resultTransitivity == True):
            equivalence += 1
        if (resultSymmetric == True):
            equivalence += 1
            return equivalence

    return equivalence

resultEquivalence = checkEquivalence()
if resultEquivalence == 3:
    print('relation is equivalent')
else:
    print('relation is not equivalent')


def checkPartialOrder():
    partialOrder = 0
    for i in range(1):
        if (resultReflective == True):
            partialOrder += 1
        if (resultTransitivity == True):
            partialOrder += 1
        if (resultAntisymmetric == True):
            partialOrder += 1
            return partialOrder

    return partialOrder

resultPartialOrder = checkPartialOrder()
if resultPartialOrder == 3:
    print('relation is partial order')
else:
    print('relation is not partial order')


def checkStrictOrder():
    strictOrder = 0
    for i in range(1):
        if (resultTransitivity == True):
            strictOrder += 1
        if (resultAsymmetric == True):
            strictOrder += 1
            return strictOrder

    return strictOrder

resultStrictOrder = checkStrictOrder()
if resultStrictOrder == 3:
    print('relation is strict order')
else:
    print('relation is not strict order')

print()


print('Завдання 2')
def reflectiveClosure(m):
    m1 = m
    for i in range(len(m1)):
        m1[i][i] = 1

    return m1

print('reflective сlosure')
print(reflectiveClosure(m))


def symmetricalClosure(m):
    m1 = m
    for i in range(len(m1)):
        for j in range(len(m1)):
            if not i == j:
                if m1[i][j] == 1:
                    m1[j][i] = 1

    return m1

print('symmetrical closure')
print(symmetricalClosure(m))


def transitiveClosure(m):
    m1 = m
    for i in range(len(m1)):
        for j in range(len(m1)):
            if not i == j:
                if m1[i][j] == 1:
                    for k in range(len(m1)):
                        m1[i][k] = m1[i][k] | m1[j][k]

    return m1

print('transitive closure')
print(transitiveClosure(m))

print()


print('Завдання 3')
def getComposition(r1, r2):
    length = len(r1)
    r = np.zeros((length, length))
    for a in range(length):
        for b in range(length):
            for c in range(length):
                if (r1[a][c] == 1) & (r2[c][b] == 1):
                    r[a][b] = 1
                    break

    return r

r1 = [
    [1,1,1,1,0],
    [1,0,1,1,1],
    [1,1,0,0,1],
    [1,1,1,0,0],
    [0,1,1,1,1]
]

r2 = getComposition(r1, r1)

r3 = getComposition(r2, r1)

print('2 degree of the given relation')
print(r2)
print('3 degree of the given relation')
print(r3)
print()
