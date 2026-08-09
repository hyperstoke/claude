"""
Самый длинный

На вход программе подаётся строка текста. Напишите программу, использующую
списочное выражение, которая находит длину самого длинного слова.

Формат входных данных: строка текста (слова разделены пробелом).
Формат выходных данных: одно число — длина самого длинного слова.

Пример входа:
"beegeek stepik python"

Пример выхода:
"7"   # самое длинное слово — beegeek
"""

text = input().split()
print(len(max(text, key=len)))

for i in range(len(text) - 1):
    min_index = i
    for j in range(i + 1, len(text)):
        if len(text[j]) < len(text[min_index]):
            min_index = j
    text[i], text[min_index] = text[min_index], text[i]
print(text)

