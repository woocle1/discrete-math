def task1():
    print('Завдання 1')
    u = {1, 2, 3, 4, 5, 6, 7, 8}
    a = set()
    b = set()

    lengthA = int(input('Введіть кількість елементів множини A: '))

    for i in range(0, lengthA):
        number = int(input('Введіть елемент: '))
        a.add(number)

    lengthB = int(input('Введіть кількість елементів множини B: '))

    for i in range(0, lengthB):
        number = int(input('Введіть елемент: '))
        b.add(number)

    union = set()
    for i in a:
        if i not in b:
            union.add(i)

    for i in b:
        union.add(i)
    print('Обʼєднання множин а та b:', union)

    intersection = set()
    for i in a:
        if i in b and i in a:
            intersection.add(i)
    print('Перетин множин а та b:', intersection)

    difference1 = set()
    for i in a:
        if i not in b:
            difference1.add(i)
    print('Різниця множин а та b:', difference1)

    difference2 = set()
    for i in b:
        if i not in a:
            difference2.add(i)
    print('Різниця множин b та a:', difference2)

    add1 = set()
    for i in u:
        if i not in a:
            add1.add(i)
    print('Доповнення множини a:', add1)

    add2 = set()
    for i in u:
        if i not in b:
            add2.add(i)
    print('Доповнення множини b:', add2)

    union = set()
    for i in difference1:
        if i not in difference2:
            union.add(i)

    for i in difference2:
        union.add(i)
    print('Симетрична різниця множин:', union)

    product = []
    for i1 in a:
        for i2 in b:
            d = i1, i2
            product.append(d)
    print('Декартовий добуток множин:', product)

def task2():
    print('Завдання 2')
    u = {1, 2, 3, 4, 5, 6, 7, 8}
    a = set()
    b = set()

    lengthA = int(input('Введіть кількість елементів множини A: '))

    for i in range(0, lengthA):
        number = int(input('Введіть елемент: '))
        a.add(number)

    lengthB = int(input('Введіть кількість елементів множини B: '))

    for i in range(0, lengthB):
        number = int(input('Введіть елемент: '))
        b.add(number)

    if a == b:
        print('Множини рівні')
    else:
        print('Множини не рівні')

    if a.issubset(b) == True:
        print('Множина а є підмножиною множини b')
    else:
        print('Множина а не є підмножиною множини b')

    if b.issubset(a) == True:
        print('Множина b є підмножиною множини a')
    else:
        print('Множина b не є підмножиною множини a')

def task3():
    print('Завдання 3')
    u = {1, 2, 3, 4, 5, 6, 7, 8}
    a = set()
    b = set()

    lengthA = int(input('Введіть кількість елементів множини A: '))

    for i in range(0, lengthA):
        number = int(input('Введіть елемент: '))
        a.add(number)

    lengthB = int(input('Введіть кількість елементів множини B: '))

    for i in range(0, lengthB):
        number = int(input('Введіть елемент: '))
        b.add(number)

    bit_string_a = ''
    bit_string_b = ''

    for number in list(u):
        if (number in a):
            bit_string_a += '1'
        else:
            bit_string_a += '0'

        if (number in b):
            bit_string_b += '1'
        else:
            bit_string_b += '0'
    
    print('Бітовий рядок множини A:')
    print(bit_string_a)
    print('Бітовий рядок множини B:')
    print(bit_string_b)


def bit_string_to_set(bit_string):
    u = {1, 2, 3, 4, 5, 6, 7, 8}
    result = set()
    for i in range(0, len(bit_string)):
        if (bit_string[i] == '1'):
            result.add(list(u)[i])

    return result

def task4(bit_string_a, bit_string_b):
    bit_string_union = ''

    for i in range(0, len(bit_string_a)):
        bit_string_union += str(int(bit_string_a[i]) | int(bit_string_b[i]))

    set_union = bit_string_to_set(bit_string_union)

    print('Обʼєднання множин:')
    print(set_union)

    bit_string_intersection = ''

    for i in range(0, len(bit_string_a)):
        bit_string_intersection += str(int(bit_string_a[i]) & int(bit_string_b[i]))

    set_intersection = bit_string_to_set(bit_string_intersection)

    print('Перетин множин:')
    print(set_intersection)

    bit_string_symmetric_difference = ''

    for i in range(0, len(bit_string_a)):
        bit_string_symmetric_difference += str(int(bit_string_a[i]) ^ int(bit_string_b[i]))

    set_symmetric_difference = bit_string_to_set(bit_string_symmetric_difference)

    print('Симетрична різниця множин:')
    print(set_symmetric_difference)

    bit_string_difference = ''

    for i in range(0, len(bit_string_a)):
        bit_string_difference += str(int(bit_string_a[i]) & ~int(bit_string_b[i]))

    set_difference = bit_string_to_set(bit_string_difference)

    print('Різниця множин:')
    print(set_difference)


# task1()

# task2()

# task3()

task4('10110011', '11100111')