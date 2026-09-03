"""
Задача: Биномиальный коэффициент

Напишите функцию compute_binom(n, k), которая принимает два натуральных
числа n и k и ВОЗВРАЩАЕТ значение биномиального коэффициента:

    n! / (k! * (n - k)!)

Факториал: n! = 1 * 2 * 3 * ... * n.

Примечание: можно завести вспомогательную функцию factorial(n) или взять
готовую math.factorial. compute_binom(n, k) должна возвращать ЦЕЛОЕ число.

Вход: два числа-аргумента n и k (натуральные), input() не нужен
Выход: функция ничего не печатает, а возвращает целое число

Пример вызова:
print(compute_binom(5, 2))
print(compute_binom(10, 0))

Вывод:
10
1
"""
import math


def compute_binom(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


n, k = int(input()), int(input())


print(compute_binom(n, k))
