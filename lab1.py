def task1():
    a = int(input())
    b = int(input())
    print('Площа =', a * b)
    print('Периметр =', 2 * (a + b))


def task2():
    import math

    a = int(input())
    b = int(input())
    print('Середнє геометричне =', math.sqrt(a * b))


def task3():
    x1, y1 = int(input()), int(input())
    x2, y2 = int(input()), int(input())

    print('Площа прямокутника =', abs(x2 - x1) * abs(y2 - y1))
    print('Периметр прямокутника =', 2 * (abs(x2 - x1) + abs(y2 - y1)))


def task4():
    a = int(input())

    if (a % 2 == 0):
        print('Число', a ,'парне')
    else:
        print('Число', a ,'непарне')


def task5():
    a = int(input())
    b = int(input()) 
    c = int(input())

    if (a < b < c):
        print('Висловлення "a<b<с" правильне')
    else: 
        print('Висловлення "a<b<с" не правильне')

    if (a > 0) or (b > 0) or (c > 0):
        print('Висловлення "хоча б одне з чисел додатне" правильне')
    else:
        print('Висловлення "хоча б одне з чисел додатне" не правильне')

    if ((a > 0) and (b < 0 and c < 0)) or ((b > 0) and (a < 0 and c < 0)) or ((c > 0) and (a < 0 and b < 0)):
        print('Висловлення "рівно одне з чисел додатне" правильне')
    else:
        print('Висловлення "рівно одне з чисел додатне" не правильне')


def task6():
    x, y = int(input()), int(input())

    if ((x + y) % 2 == 0):
        print('True')
    else:
        print('False')


def task7():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if (abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2):
        print('Yes')
    else:
        print('No')
