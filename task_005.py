# Напишите программу, которая на вход принимает число 
# и проверяет кратно ли оно 10 или 15, но не 30.

a = int(input('Введите число: '))

if (a % 30 != 0 and a % 10 == 0):
    print(a, 'кратно 10, но не кратно 30')
elif a % 30 != 0 and a % 15 == 0:
    print(a, 'кратно 15, но не кратно 30')
else:
    print('число или не кратно 10 и 15, или кратно 30')