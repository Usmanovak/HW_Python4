'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.

2 2
4 
'''

first_num = int(input('Enter a: '))
second_num = int(input('Enter b: '))

def summa(first_num, second_num):
    if first_num == 0:
        return second_num
    return summa(first_num-1, second_num+1)

print(summa(first_num, second_num))
