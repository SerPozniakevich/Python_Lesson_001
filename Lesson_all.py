# LESSON 2
#____________________________________________________
# # Подсчёт конкретных символов в строке

# string_text = "Посчитайте сколько раз символ встречается в строке"

# count = 0
# sim = input('Введите символ: ')
# for i in string_text:
#     if i == sim:
#         count += 1
# print(count)

# Задано кол-во секунд, перевести в дни, часы, минуты, секунды.

# Var may

# time = int(input('Введите количество секунд: '))
# day = time // (60*60*24)
# hour = (time % (60*60*24)) // (60 * 60)
# minuty = ((time % (60*60*24)) % (60 * 60)) // 60
# sec = (((time % (60*60*24)) % (60 * 60)) % 60) % 60
# print (f'{day} дней, {hour} часов, {minuty} минут, {sec}')

# Var 2

# time = int(input('Введите количество секунд: '))
# ss = time % 60 # секунды - остаток от деления на 60
# time //= 60 # целечисленное деление на 60 - время без секунд
# mm = time % 60 # минуты - остаток от деления на 60
# time //= 60 # целечисленное деление на 60 - время без минут
# hh = time % 24 # часы - остаток от деления на 24
# time //= 24 # целечисленное деление на 24 - время без часов (дни)
# dd = time 
# print (f'{dd} дней, {hh} часов, {mm} минут, {ss}')

# Var thuter

# time = int(input('Введите количество секунд: '))
# min, sec = time // 60, time % 60 #
# hour, min = min // 60, min % 60 #
# day, hour = hour // 24, hour % 24 #
# print (f':{day} dd :{hour} hh :{min} mm :{sec} ss')

# Напишите программу, которая принимает на вход число N и выдаёт паследовательность  из N членов/
# N = 5: 1, -3, 9, -27, 81

# Var 1

# n = int(input('Введите N: '))
# for i in range(n):
#     print((-3) ** i, end= " ")

# Var 2

# n = int(input('Введите N: '))
# num = 1
# for i in range(n):
#     print(num, end= " ")
#     num *= -3

# LESSON 2_1
#______________________________________________

# n = int(input('Введите N: '))
# j = 1
# list_n = []   # задаём пустой список
# for i in range(1, n + 1):
#     list_n.append(str(j)) # Заполнение списка значениями с выводом без квадратных скобок
#     j = j * -3

# print(', '.join(list_n)) # Вывод без квадратных скобок



# n = int(input('Введите N: '))
# j = 1
# list_n = []   # задаём пустой список
# for i in range(1, n + 1):
#     list_n.append(j) # Заполнение списка значениями с выводом с квадратными скобками
#     j = j * -3

# print(list_n)  # Вывод с квадратными скобками



# Напишите программу, в которой пользователь будет задавать две строки
# а программа определять количество вхождений одной строки в другой.
# пример: 1 строка: мама мыла раму
#         2 строка: мама -> вхождений 1

# str1 = input('Введите строку 1:')
# str2 = input('Введите строку 2:')
# count = str1.count(str2)
# print(count)

# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите N: '))
# d = dict() # функция создания словаря (задаём пустой словарь)
# j = 1
# for i in range(n):
#     d[j] = 3 * j + 1
#     j += 1
# print(d)


# LESSON 3_Albina
#______________________________

# Задайте список. Напишите программу, которая определит есть ли в данном списке некое число.

# Var Kamyanecky

# str1 = input('Введите строку 1:')
# str2 = input('Введите строку 2:')
# count = str1.count(str2) 
# print(count)

# Var Lesson

# str1 = input('Введите строку 1:').split()
# print('Введённый список:', str1)
# str2 = input('Введите строку 2:')

# if str2 in str1:
#     print("Число есть")
# else:
#     print('Числа нет')

# Задайте список. Напишите программу, которая определит позицию второго вхождения, либо сообщит, что её нет.

# Var Kamyanecky

# str1 = input('Введите строку 1:')
# str2 = input('Введите строку 2:')
# count = str1.count(str2)
# count = count - 1
# print(count)

# Var Lesson

from datetime import datetime
from itertools import count
from time import time


# str1 = input('Введите строку 1:').split()
# print('Введённый список:', str1)
# str2 = input('Введите строку 2:')
# print(str1.count(str2))
# count = 0
# if str1.count(str2) >= 2:
#     for i in range(len(str1)):
#         if str1[i] == str2:
#             count += 1
#             if count == 2:
#                 print("Индекс второй позиции: ", i)
# else:
#     print('-1')

# Var 3 Lesson  - НЕ РАБОТАЕТ!!!!

# str1 = input('Введите строку 1:').split()
# print('Введённый список:', str1)
# str2 = input('Введите строку 2:')
# count = 0
# for i, el in enumerate(str1): # цикл выдаёт и индексы и значения    
#     if str1 == el:
#         count += 1
#         if count == 2:
#             print("Индекс второй позиции: ", i)
# if count < 2:
#     print('-1')

# Вывод случайного числа
import time

# now = time.time()                 # Функция вызова времени для получения псевдорандомного значения
# print(now)
# print(type(now))
# print(str(now).split('.')[1][0])

# LESSON 3 YURIY
#------------------------------------------------

import datetime


# print(datetime.datetime.now().microsecond % 100) #Функция вызова времени для получения псевдорандомного значения

# Определить, присутствует ли  в заданном списке строк, некоторое число.

# text_1 = ['my', 'false', 'jgut', 'Serjio', 'true', '1']

# def find_didgit(new_text):
#     for i in range(len(new_text)):
#         if new_text[i].isdigit():     # проверка на соответствие числу
#             print(i)

# find_didgit(text_1)

# Поиск конкретного числа в строке.
#  
# text_1 = ['my', 'false', 'jgut', 'Serjio', 'true', '1']
# num1 = 1
# def find_num(new_text, num):
#     for i in range(len(new_text)):
#         if new_text[i].isdigit():     # проверка на соответствие числу
#             if int(new_text[i]) == num:
#                 print(i)

# find_num(text_1, num1)

# Поиск конкретного числа внутри строк.

# text_1 = ['my', 'false', '1jg1   ut', 'Serjio', 'true', '1dfnfh']
# num1 = 1
# def find_num(new_text, num):
#     for i in range(len(new_text)):
#         for j in new_text[i]:
#             if j.isdigit():       # проверка на соответствие числу
#                 if int(j) == num:
#                     print(i)
#                     break          # закрывет цикл, в котором находится

# find_num(text_1, num1)

# LESSON 4 YURIY SAVOS'KIN
#______________________________________

# Корень квадратного уравнения

# a, b, c = map(int,input('Введите значения a, b и с через пробел: ' ).split())
# d = b ** 2 - 4 * a * c
# if d  > 0:
#     print(f'x1 = {round((-b + d ** 0.5) / (2 * a), 2)}, x2 = {round((-b - d ** 0.5) / (2 * a), 2)}')
# elif d == 0:
#     (f'x1 = {round(-b / (2 * a), 2)}')
# else:
#     print('Корней нет')

# Найти наименьшее общее кратное.

a, b = map(int,input('Введите значения a и b через пробел: ' ).split())
nod = 2
while True:
    if a % nod == 0 and b % nod == 0:
        break
    else:
        nod += 1

nok = int(a * b / nod)
print(f' nod: {nod}, nok: {nok}')