# m = [ [1, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 0], [0, 1, 1, 1, 1] ]
m = [ [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0] ]
# m = [ [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# m = [ [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [1, 0, 0, 1, 0], [0, 0, 0, 0, 0] ]


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
