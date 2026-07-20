# Задача: «Шифр Цезаря»
#
# Шифр Цезаря — простой сдвиговый шифр. Нужно
# написать программу, которая ДЕКОДИРУЕТ (расшифровывает) сообщение,
# а не кодирует.
#
# Формат входных данных:
#   - первая строка: число n — сдвиг;
#   - вторая строка: закодированное сообщение из строчных латинских букв.
#
# Формат выходных данных:
#   - одна строка — декодированное сообщение.

shift = int(input())
encoded_text = input()

original_text = ""
alphabet_eng = "abcdefghijklmnopqrstuvwxyz"
flag = True

for letter in encoded_text:
    if letter in alphabet_eng:
        original_text += alphabet_eng[(alphabet_eng.index(letter) - shift) % 26]
    elif letter == " ":
        original_text += " "
    else:
        flag = False
        break

if flag:
    print(original_text)
else:
    print("Таких букв нет в английском языке")



