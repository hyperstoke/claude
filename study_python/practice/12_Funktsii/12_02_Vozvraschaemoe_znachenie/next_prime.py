"""
Next Prime

Напишите функцию get_next_prime(num), которая принимает в качестве аргумента
натуральное число num и возвращает первое простое число, большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

Примечание 2. Приведённый ниже код:
print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))

должен выводить:
7    # для 6
11   # для 7
17   # для 14
"""

# Проверка числа является ли ПРОСТЫМ
def is_prime(num: int) -> bool:
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

# Функция нахождения следующего после num ПРОСТОГО числа
def get_next_prime(num: int) -> int:
    candidate = num + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1


n = int(input())


print(get_next_prime(n))