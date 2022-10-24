from datetime import datetime
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

from itertools import count
from string import digits
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

# a, b = map(int,input('Введите значения a и b через пробел: ' ).split())
# nod = 2
# while True:
#     if a % nod == 0 and b % nod == 0:
#         break
#     else:
#         nod += 1

# nok = int(a * b / nod)
# print(f' nod: {nod}, nok: {nok}')

# LESSON 5 ALBINA
#_____________________________________________________

from collections import Counter
from unicodedata import digit
from unittest import result

import numpy



# items = numpy.random.randint(10, size = 10) # Параметр для заполнения списка рандомными числами
# items_set = list(items[: 10]) # Создание списка
# print(*items_set) # Печать со звёздочкой убирает квадратные скобки и запятые

# dict_new = Counter(items_set) # Counter проверяет количество повторений в списке
# res_list = [i for i in dict_new if dict_new[i] == 1] # сокращённое написание цикла ниже
# # res_list = []
# # for i in dict_new:
# #     if dict_new[i] == 1:
# #         res_list.append(i) # Заполняем список числами, которые не имеют повторений (были 1 раз)

# print(*res_list)

# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнять условие A[i] - 1 = A[i - 1]. Найдите это число.
#----------------------------------------------------------------------------------------------
# patch = r'C:\Users\User\Documents\Geekbrains\Python\Lesson01\file.task.txt' # создание пути к файлу
# # patch = 'C:\\Users\\User\\Documents\\Geekbrains\\Python\\Lesson01\\file.task.txt' # создание пути к файлу
# data = open(patch, 'r') # открытие в режиме чтения
# for line in data:  # цикл для чтения данных из файла
#     print(line)
# data.close() # разрыв связи с файлом
# line = [int(i) for i in line.split()]
# print(line)

# for i in range(1, len(line)):
#     if line[i -1] != line[i] - 1:
#         num_no = line[i - 1] + 1

# print(num_no)

#Дан список чисел. Создайте список, в который попадают числа описываемые 
# возрастающую последовательность. Порядок элементнов менять нельзя.
#-----------------------------------------------------------------------

# input_list = [1, 5, 2, 3, 4, 6, 1, 7]
# result_list = [input_list[0]]
# for i in input_list[1:]:  ## проверка с первого элемента до конца списка
#     if i > result_list[-1]:
#         result_list.append(i)

# print(*result_list)



# Напишите программу, удаляющую с текста все слова, содержащие "абв".
#-----------------------------------------------------------------------

# input_text = 'абв проабв разд вобл инжес пабвс'

# text_1 = 'абв'
# print(input_text)
# print(text_1)
# real_text = input_text.split()
# result_list = []
# for word in real_text:
#     if text_1 not in word:
#         result_list.append(word)

# print(" ".join(result_list))

# Lesson 5 Yury
#________________________________________________________
# Напишите программу, удаляющую с текста все слова, содержащие "абв".
#-----------------------------------------------------------------------
# input_text = 'абв проабв разд вобл инжес пабвс'
# new_text = ' '.join(list(filter(lambda w: 'абв' not in w, input_text.split())))
# print(new_text)

# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнять условие A[i] - 1 = A[i - 1]. Найдите это число.
#-----------------------------------------------------------------------------------------------

# num = list(map(int, '0 1 2 3 4 5 7 8 9 10'.split(' ')))

# #Var I
# #---------------------------
# # for i in range(1, len(num)):
# #     if num[i -1] != num[i] - 1:
# #         num_no = num[i] - 1

# # print(num_no)

# #Var II
# #---------------------------------------------------------

# print([num[i] - 1 for i in range(1, len(num)) if num[i] - 1 != num[i - 1]][0])

# LESSON 6 Albina
#_______________________________________________________________________

# Алгоритм ПОЛЬСКОЙ записи арифметического выражения
#------------------------------------------------------


# input_list = input('Введите выражение: ').split()
# output = []
# stack_list = []
# for elem in input_list:
#     if elem.isdigit():
#         output.append(elem)
#     elif elem == "(": # помещаем в стек (забираем с последнего)
#         stack_list.append(elem)
#     elif elem == ")":
#         while stack_list and stack_list[- 1] != "(":
#             output.append(stack_list.pop()) # забираем поеследний элемент из стека
#         if not stack_list:
#             print('Несогласованные скобки')
#             exit()
#         stack_list.pop()
#     elif elem in ["*", "/"]:
#         while stack_list and stack_list[- 1] in ["*", "/"]:
#             output.append(stack_list.pop())
#         stack_list.append(elem)
#     elif elem in ["+", "-"]:
#         while stack_list and stack_list[- 1] in ["*", "/", "+", "-"]:
#             output.append(stack_list.pop())
#         stack_list.append(elem)
#     else:
#         print('Нераспознанный знак')
#         exit()
# while stack_list:
#     if stack_list[- 1] not in ["*", "/", "+", "-"]:
#         print('Нераспознанный знак')
#         exit()
#     output.append(stack_list.pop())
# print(output)

# res = []

# for elem in output:
#     if elem.isdigit():
#         res.append(int(elem))
#     else:
#         b = res.pop()
#         a = res.pop()
#         if elem == "+":
#             res.append(a + b)
#         elif elem == "-":
#             res.append(a - b)
#         elif elem == "*":
#             res.append(a * b)
#         elif elem == "/":
#             res.append(a / b)
# print(res)

# LESSON 6 Yury
#_________________________________________________

# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# mult = '*'
# div = '/'
# plus = '+'
# minus = '-'

# evaluation = '2 + 2 * 2 / 2 - 2'
# eval_list = evaluation.split()
# i = 0
# res = 0
# while len(eval_list) != 1:
#     while True:
#         print(eval_list)
#         el = eval_list[i]
#         if el == mult or el == div:
#             if el == mult:
#                 res = float(eval_list[i - 1]) * float(eval_list[i + 1])
#             else:
#                 res = float(eval_list[i - 1]) / float(eval_list[i + 1])
#             eval_list[i] = str(res)
#             eval_list.pop(i + 1)
#             eval_list.pop(i - 1)
#             i = 0
#             if mult and div not in eval_list:
#                 break
#         else:
#             i += 1


#     while True:
#         print(eval_list)       
#         el = eval_list[i] 
#         if el == plus or el == minus:
#             if el == plus:
#                 res = float(eval_list[i - 1]) + float(eval_list[i + 1])
#             else:
#                 res = float(eval_list[i - 1]) - float(eval_list[i + 1])
#             eval_list[i] = str(res)
#             eval_list.pop(i + 1)
#             eval_list.pop(i - 1)
#             i = 0
#             if plus and minus not in eval_list:
#                 break
#         else:
#             i += 1

# print(res)

# LESSON 007 Yury
#____________________________________________________________________________

print(f'{datetime.now().strftime("%d.%m.%Y. %H:%M")}')