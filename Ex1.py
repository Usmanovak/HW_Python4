'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит 
число А в целую степень B с помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''

number = int(input('Enter number: '))
power = int(input('Enter power: '))

def power_num(number, power):
    if power == 1:
        return number
    return number * power_num(number, power - 1)

print(power_num(number, power))