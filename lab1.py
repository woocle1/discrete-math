import math
import statistics

def task1(a, b):
    print('Завдання 1')
    print('Площа =', a * b)
    print('Периметр =', 2 * (a + b))
    print()


def task2(a, b):
    print('Завдання 2')
    print('Середнє геометричне =', (a * b) ** 0.5)
    print()


def task3(x1, y1, x2, y2):
    print('Завдання 3')
    print('Площа прямокутника =', abs(x2 - x1) * abs(y2 - y1))
    print('Периметр прямокутника =', 2 * (abs(x2 - x1) + abs(y2 - y1)))
    print()


def task4(a):
    print('Завдання 4')
    if (a % 2 == 0):
        print('Число', a ,'парне')
    else:
        print('Число', a ,'непарне')
    print()


def task5(a, b, c):
    print('Завдання 5')
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
    print()


def task6(x, y):
    print('Завдання 6')
    if ((x + y) % 2 == 0):
        print('Поле з кординатами', x, ',', y, 'біле')
    else:
        print('Поле з кординатами', x, ',', y, 'чорне')
    print()


def task7(x1, y1, x2, y2):
    print('Завдання 7')
    if ((abs(x1 - x2) == abs(y1 - y2)) or (x1 == x2 or y1 == y2)):
        print('Ферзь за один хід може перейти з поля', x1, ',', y1, 'на поле', x2, ',', y2)
    else:
        print('Ферзь за один хід не може перейти з поля', x1, ',', y1, 'на поле', x2, ',', y2)
    print()


def task8(a, b):
    print('Завдання 8')
    print('Цілі числа в діапазоні', a, '-', b)
    for i in range(a, b + 1):
        print(i)
    print('Кількість цілих чисел в діапазоні', a, '-', b, '=', b - a + 1)
    print()


def task9(n):
    print('Завдання 9')
    n_length = len(str(n))
    result_str = ''
    for i in range(n_length):
        result_str = (result_str + str((n % 10)))
        n = n // 10
    print(result_str)
    print()


def task10(a):
    print('Завдання 10')
    for i in range(0, len(a)):
        b = statistics.mean(a)
        if a[i] > b:
            print(a[i] - 18)
    print()


def task11(n):
    print('Завдання 11')
    result = True 
    for i in range(2, n):
        if (n % i) == 0:
            result = False
            break
    if result == True:
        print('Число', n, 'є простим')
    elif result == False:
        print('Число', n, 'не є простим')
    print()


def task12(x, y, z):
    print('Завдання 12')
    print('Значення фунції =', math.log10((z ** 2) + y) + (math.fabs(z ** 2 - y)) + (x ** 2))
    print()


def task13():
    print('Завдання 13')
    name = input()
    surname = input()
    mobile_phone = input()

    # if name == '' or surname == '' or mobile_phone == '':
    #     print('Не залишайте жодні поля порожніми')
    # else:
    #     print('Спасибі')
    
    # if name or surname or mobile_phone:
    #     print('Спасибі')
    # else:
    #     print('Не залишайте жодні поля порожніми')

    # if (name and surname):
    #     print('Спасибі')
    # else:
    #     print('Не залишайте жодні поля порожніми')
    print()


def task14():
    print('Завдання 14')
    for i in range(5):
        a = int(input())
        if a == 5:
            print('Молодець, гарний вибір')
            break
    print()


def task15():
    print('Завдання 15')
    print('Числа, які націло діляться на 13')
    for i in range(13, 100, 13):
        print(i)
    print()


def task16():
    print('Введіть перший рядок')
    a = input()
    print('Введіть другий рядок')
    b = input()
    print('Введіть символ, який хочете вставити')
    n = input()
    print(a + b)
    print(a * 10)
    print(a[:1], n, a[1:], sep='')


# task1(5, 9)
# task2(12, 3)
# task3(1, 1, 6, 6)
# task4(7)
# task5(-7, -2, 8)
# task6(6, 6)
# task7(4, 4, 7, 7)
# task8(15, 20)
# task9(987)
# task10([1, 9, 76, 13])
# task11(13)
# task12(5, 10, 1.25)
# task13()
# task14()
# task15()
# task16()
