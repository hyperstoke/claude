"""
Используя списочное выражение, дополните приведённый код так, чтобы получить
новый список, содержащий строки исходного списка, где у каждой строки удалён
первый символ.

Вход: готовый список keywords (задан в коде).
Выход: печать нового списка new_keywords.

Пример:
['False', 'True', 'None']   # исходный список
['alse', 'rue', 'one']      # что должно получиться
"""

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', \
            'break', 'class', 'continue', 'def', 'del', 'elif', 'else', \
            'except', 'finally', 'try', 'for', 'from', 'global', 'if', \
            'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', \
            'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [element[1::] for element in keywords]

print(new_keywords)
