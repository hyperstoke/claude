"""
Проект: Генератор безопасных паролей

Мини-проект раздела "Модуль random": собрать целую программу из кусочков —
модуль random, цикл for, функции, условный оператор, ввод/вывод, целые числа.

Что делает программа:
1. генерирует заданное количество паролей;
2. умная настройка длины пароля;
3. настройка того, какие символы включать в пароль, а какие исключать.
"""

import random

DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"


# Функция проверяет вводимое значение, оно должно быть больше 0
# и возвращает его
def input_valid_digit() -> int:
    while True:
        num = input()
        if num.isdecimal() and int(num) > 0:
            return int(num)
        print("Заданное число должно быть больше 0")
        print("Введите новое значение: ", end="")


# Функция проверяет вводимое значение, оно должно быть y или n
# Врзвращает True или False соответственно
def input_flag() -> bool:
    while True:
        answer = input()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        print("Вы должны ввести (y/n): ", end="")


# Функция для генерации пароля через цикл, он идет по длине пароля
# на каждую позицию он берет рандомное значение из alphabet
def generate_password(length: int, alphabet: str) -> str:
    g_pass = ""
    for _ in range(length):
        g_pass += random.choice(alphabet)
    return g_pass


print('Добро пожаловать в "Генератор паролей"')

# Кол-во паролей и их длина проходит проверку в функции input_valid_digit()
print("Введите генерируемое кол-во паролей: ", end="")
count_pass = input_valid_digit()

print("Введите длину генерируемых паролей: ", end="")
length_pass = input_valid_digit()

# Создание бесконечного цикла, пока не будет выполнено условие "not any"
# Флаги возвращаются из функции input_flag()
while True:
    print("Должен ли пароль содержать цифры, (y/n): ", end="")
    contain_digit_flag = input_flag()

    print("Включать ли прописные буквы, (y/n): ", end="")
    contain_upper_flag = input_flag()

    print("Включать ли строчные буквы, (y/n): ", end="")
    contain_lower_flag = input_flag()

    print("Включать ли символы, (y/n): ", end="")
    contain_symbol_flag = input_flag()

# Если хоть один флаг не True цикл начинается заново
    if not any((contain_digit_flag, contain_upper_flag,
                contain_lower_flag, contain_symbol_flag)):
        print("Нужно выбрать хотя бы один набор символов!")
        continue
    break

# Собираем алфавит для генерации пароля
alphabet = ""
if contain_digit_flag:
    alphabet += DIGITS
if contain_upper_flag:
    alphabet += UPPERCASE_LETTERS
if contain_lower_flag:
    alphabet += LOWERCASE_LETTERS
if contain_symbol_flag:
    alphabet += PUNCTUATION


print("Генерирую пароли:")
# Цикл для создания паролей и их вывода
for _ in range(count_pass):
    generated = generate_password(length_pass, alphabet)
    print(generated)