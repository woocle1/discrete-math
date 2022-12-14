def graphOrientation(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if y > x:
                if not matrix[x][y] == matrix[y][x]: "Граф орієнтований"
    return "Граф може бути як неорієнтованим, так і орієнтованим"