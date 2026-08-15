"""
Задача: Отсортируй и выведи

Напишите функцию print_sorted_hyphen(s), которая принимает строку s,
состоящую из слов, разделённых дефисами, и выводит эти слова на одной
строке в лексикографическом порядке, разделённые дефисами.

Примечание: гарантируется, что в последовательности будет более одного слова.

Вход: строка-аргумент s — приходит в функцию, input() не нужен
Выход: одна строка — слова по алфавиту через дефис

Пример вызова:
print_sorted_hyphen("orange-apple-avocado-plum-cherry")

Вывод:
"apple-avocado-cherry-orange-plum"
# в файле образец показан в кавычках; печатать кавычки не нужно
"""


def print_sorted_hyphen(text):
#    words = text.split("-")
#    words.sort()
#    print("-".join(words))
    print("-".join(sorted(text.split("-"))))


text = input()

print_sorted_hyphen(text)
