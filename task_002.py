# Напишите программу, которая на вход принимает 5 чисел (можно списком) и 
# находит максимальное из них.

#Var 1
# a = list(input('Введите ряд чисел: '))
# max_number = a[0]
# for i in a:
#     if i > max_number:
#         max_number = i
# print(max_number)

# Var 2
# list_entered = input('Введите ряд чисел через пробел: ').split() # split разбивает список по пробелам
# list_number = list(map(int, list_entered)) # "map" - приводит в соответствие вида, например в "int"
# print(max(list_number)) # max - внутр.функция питон, вывод максимального значения списка/строки