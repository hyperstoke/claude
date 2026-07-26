# Задача: «Самое тяжёлое слово»
#
# Под «тяжестью» слова будем понимать сумму кодов по таблице Unicode всех
# символов этого слова. Напишите программу, которая принимает 4 слова и
# находит среди них самое тяжёлое слово. Если самых тяжёлых слов будет
# несколько, программа должна вывести первое из них.
#
# Формат входных данных: 4 слова, каждое на отдельной строке.
# Формат выходных данных: самое тяжёлое слово.

max_weight_word = ""
max_weight_count = 0

for _ in range(4):
    weight_count = 0
    word = input()

    for i in word:
        weight_count += ord(i)

    if weight_count > max_weight_count:
        max_weight_count = weight_count
        max_weight_word = word

print(max_weight_word)