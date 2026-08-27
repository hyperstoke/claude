"""
Используя списочное выражение, дополните приведённый код так, чтобы получить
новый список, содержащий длины строк исходного списка.

Вход: готовый список keywords (задан в коде).
Выход: печать списка lengths.

Пример:
['False', 'True', 'None']   # исходный список
[5, 4, 4]                   # что должно получиться
"""

keywords = [
    'False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for',
    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
    'pass', 'raise', 'return', 'while', 'yield'
]

lengths = [len(element) for element in keywords]

print(lengths)
