# Напишите программу, которая будет на вход принимать дробь и показывать первую цифру дробной части числа.



import string
from unittest import result

# Var 1

# a = float(input('Введите десятичную дробь: '))
# a = str(a % 1) # перевод в строку и обнуление целого числа (остаются только числа после запятой)
# print(a[2]) # вывод на печать третьего символа массива

#Var 2

# a = float(input('Введите десятичную дробь: '))
# a = int(a * 10)
# result = a % 10
# if result == 0:
#     print('NO')
# else:
#     print(result)

# Var 3

a = float(input('Введите десятичную дробь: '))
a = int((a * 10) % 10)

print(a)
