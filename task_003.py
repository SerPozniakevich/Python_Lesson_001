# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.

# Var 1

# a = int(input('Введите число: '))
# list_num = range(-a, a + 1)
# s = ' ' # переменная для вывода в одну строку
# for i in list_num:
#     s = s + ' ' + str(i) + ',' # подготовка к выводу одной строки
# print(s[1:])

# Var 2

a = int(input ('Введите число: '))
list_num = list(range(-a, a + 1)) # list - запись в одну строку ввиде массива в []
print(list_num)