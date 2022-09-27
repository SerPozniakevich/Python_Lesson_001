# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.

a = int(input('Введите число: '))
list_num = range(-a, a + 1)
for i in list_num:
    print(i)