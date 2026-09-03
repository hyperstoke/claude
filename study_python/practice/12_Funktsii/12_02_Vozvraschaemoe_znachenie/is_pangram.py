"""
Задача: Панграммы

Панграмма — фраза, содержащая все буквы алфавита (её используют для показа
шрифтов). Напишите функцию is_pangram(text), которая принимает строку текста
на английском языке и ВОЗВРАЩАЕТ True, если текст — панграмма, иначе False.

Примечание: гарантируется, что в строке только буквы английского алфавита
и пробелы (регистр может быть любой).

Вход: один аргумент text — строка, input() не нужен
Выход: функция ничего не печатает, а возвращает True или False

Пример вызова:
print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))

Вывод:
True
True
False
"""


def is_pangram(text):
    text = text.lower()
    return all(letter in text for letter in "abcdefghijklmnopqrstuvwxyz")


print(is_pangram(input()))
