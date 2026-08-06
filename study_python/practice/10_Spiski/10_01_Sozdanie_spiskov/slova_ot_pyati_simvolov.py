"""
Используя списочное выражение, дополните приведённый код так, чтобы получить
новый список, содержащий только слова длиной не менее пяти символов
(включительно).

Вход: готовый список keywords (задан в коде).
Выход: печать списка new_keywords.

Пример:
['False', 'True', 'None', 'assert']   # исходный список
['False', 'assert']                   # что должно получиться
"""

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [element for element in keywords if len(element) >= 5]

print(new_keywords)
