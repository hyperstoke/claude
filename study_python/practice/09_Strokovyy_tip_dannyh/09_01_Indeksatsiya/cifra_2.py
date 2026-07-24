# Stepik 9.2 — "Цифра 2"
# Дано: строка.
# Нужно: вывести "Цифра", если в строке есть хотя бы одна цифра, иначе "Цифр нет".

text = input()

for i in text:
    if i.isdigit():
        print("Цифра")
        break
else:
    print("Цифр нет")


