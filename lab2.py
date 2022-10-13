from random import randrange
import random
import numpy as np
import statistics
import numpy
from datetime import datetime

def task1():
    print('Завдання 1')
    a = [i for i in range(1000)]
    print(a)
    print()


def task2(*args):
    print('Завдання 2')
    a = np.array([*args])
    print(a)
    print()


def task3(a):
    print('Завдання 3')
    def sort_max(a):
        a.sort(reverse = True)
        print(a)
    def sort_min(a):
        a.sort(reverse = False)
        print(a)
        print()
    sort_max(a)
    sort_min(a)


def task4(a, b):
    print('Завдання 4')
    # sum = a + b
    # sum.sort()
    # print(sum)

    a += b
    print(a)
    print()


def task5(n):
    print('Завдання 5')
    a = []
    for i in range(n):
        b = random.randrange(1, n)
        if b not in a:
            a.append(b)
    print(a)
    print()


def task6():
    print('Завдання 6')
    a = np.arange(1, 101)
    print(a.reshape((10,10)))
    print()


def task7():
    print('Завдання 7')
    a = np.arange(1, 101)
    a.reshape((10,10))
    print(np.array2string(a))
    print()


def task8():
    print('Завдання 8')
    a = np.arange(1, 101)
    b = a.reshape(100, 1)
    print(b)
    print()


def task9():
    print('Завдання 9')
    a = np.array([1, 2, 3] * 10)
    print(a)
    print()


def task10():
    print('Завдання 10')
    x = np.zeros((10, 10))
    print(x)
    print()


def task11():
    print('Завдання 11')
    matrix = np.array(
        [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    )
    print(matrix.max(axis = 0))
    print(matrix.min(axis = 0))
    print(matrix.max(axis = 1))
    print(matrix.min(axis = 1))
    print()


def task12(a):
    print('Завдання 12')
    for i in range(1, len(a)):
        if a[i] == max(a):
            print(i)
    print()


def task13(list1, list2):
    print('Завдання 13')
    a = []
    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                a.append(i1)
    print(a)
    print()


def task14():
    print('Завдання 14')
    month = ['December', 'January', 'February', 
            'March', 'April', 'May', 
            'June', 'July', 'August', 
            'September', 'October', 'November']

    winter = []
    for i in range(0, len(month)):
        if month[i] == 'January' or month[i] == 'February' or month[i] == 'December':
            winter.append(month[i])
    
    spring = []
    for i in range(0, len(month)):
        if month[i] == 'March' or month[i] == 'April' or month[i] == 'May':
            spring.append(month[i])
    summer = []
    for i in range(0, len(month)):
        if month[i] == 'June' or month[i] == 'July' or month[i] == 'August':
            summer.append(month[i])

    autumn = []
    for i in range(0, len(month)):
        if month[i] == 'September' or month[i] == 'October' or month[i] == 'November':
            autumn.append(month[i])
           
    print(tuple(winter))
    print(tuple(spring))
    print(tuple(summer))
    print(tuple(autumn))
    print()


def task15():
    print('Завдання 15')
    my_tuple = (
        ["Andrii", "08.05.2005"],
        ["Jack", "08.02.2005"],
        ["Mary", "08.05.2004"]
    )
    print(tuple(sorted(my_tuple, key = lambda t : datetime.strptime(t[1], '%d.%m.%Y'))))
    print()


print('Завдання 16')
products = (['apple', 25, 17],
            ['cheese', 150, 2],
            ['bread', 28, 9])

request = (
    ('appLe', 2),
    ('cheese ', 1),
    ('brEad', 6),
)

def totalPrice(order):
    total = 0
    for i in range(len(order)):
        match order[i][0].lower().replace(" ", ""):
            case 'apple':
                if order[i][1] > products[i][2]:
                    print(-1)
                    continue
                else:
                    total += order[i][1] * products[i][1]
                    products[i][2] -= order[i][1]
            case 'cheese':
                if order[i][1] > products[i][2]:
                    print(-1)
                    continue
                else:
                    total += order[i][1] * products[i][1]
                    products[i][2] -= order[i][1]
            case 'bread':
                if order[i][1] > products[i][2]:
                    print(-1)
                    continue
                else:
                    total += order[i][1] * products[i][1]
                    products[i][2] -= order[i][1]
            case _:
                print(-2)
    return total

print(totalPrice(request))


print('Завдання 17')
class Student:
    def __init__(self, name ="John Doe", courses =[], phone_number = '', email_address = '', degree = 'Вachelor'): 
        self.name = name
        self.courses = courses
        self.phone_number = phone_number
        self.email_address = email_address
        self.degree = degree
        print("Створено об’єкт для "+ name)

    def printDetails(self):
        print("Ім’я: ", self.name)
        print("Курси: ", self.courses)
        print("Номер телефону: ", self.phone_number)
        print("Електронна пошта: ", self.email_address)
        print("Освіта: ", self.degree)
    def enroll(self, course):
        self.courses.append(course)

student1 = Student("Mary", ["L548"])

print("Уведіть курси, які вивчає", student1.name) 
newcourse = input ("Уведіть номер курсу або 'stop' ")

while newcourse != "stop":
    student1.enroll(newcourse)
    print("Уведіть курси, які вивчає", student1.name) 
    newcourse = input ("Уведіть номер курсу або 'stop' ")
    student1.printDetails()

student2 = Student("Andrii", ["L548"], '+380000000000', '@ukr.net')

student2.printDetails()


print('Завдання 18')
class Employee:
    def __init__(self, name = "John", salary = 30000, experience = 5, department = 'support'): 
        self.name = name
        self.salary = salary
        self.experience = experience
        self.department = department
        print("Створено об’єкт для " + name)

    def printDetails(self):
        print("Ім’я: ", self.name)
        print("Заробітна плата: ", self.salary)
        print("Досвід роботи: ", self.experience, 'years')
        print("Відділ: ", self.department)

    def changeDepartment(self):
        self.department = input('Уведіть новий відділ для Andrii: ')

employee1 = Employee("John", 30000, 5)
employee1.printDetails()

employee2 = Employee('Andrii', 50000, 3)
employee2.changeDepartment()
employee2.printDetails()


task1()

task2(30, 20, 13, 10)

task3([-3, 4, 100, 1, 3])

task4([1, 2, 3, 4, 5], [-2, 0, 15, 25, 40])

task5(12)

task6()

task7()

task8()

task9()

task10()

task11()

task12([12, 5, 90, 3])

task13(['Python', 'Java', 'JavaScript', 'Swift'], ['C++', 'Swift', 'JavaScript'])

task14()

task15()