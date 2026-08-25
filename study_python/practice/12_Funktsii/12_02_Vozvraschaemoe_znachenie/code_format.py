"""
Задача: <code>

Напишите функцию code_format(text), которая принимает строку текста text,
оборачивает её в теги <code></code> и ВОЗВРАЩАЕТ результат.

Вход: строка-аргумент text — приходит в функцию, input() не нужен
Выход: функция ничего не печатает, а возвращает строку (печатает вызывающий код)

Пример вызова:
print(code_format('s = input()'))
print(code_format('15'))
print(code_format('None'))

Вывод:
"<code>s = input()</code>"
"<code>15</code>"
"<code>None</code>"
# в файле образец показан во внешних кавычках; печатать их не нужно
# теги <code> и </code> — обычный текст, никакой магии в них нет
"""


def code_format(code):
    return f'<code>{code}</code>'


text = input()

print(code_format(text))