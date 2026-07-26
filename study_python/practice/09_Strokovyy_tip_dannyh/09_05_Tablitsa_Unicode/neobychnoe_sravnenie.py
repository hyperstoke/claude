"""
Задача: «Необычное сравнение»

На вход подаются 2 строки. Нужно сравнить их посимвольно, не учитывая
регистр и игнорируя все небуквенные символы. Вывести "YES", если строки
окажутся равны при такой проверке, иначе "NO".

Формат входных данных:
    2 строки, каждая на отдельной строке.

Формат выходных данных:
    "YES" или "NO" в соответствии с условием задачи.

Примечание. Пример теста:
    "Ab4c1$#ddd"
    "a_b_c##DDD70"
    -> "YES"
"""

line_one = "".join(i for i in input() if i.isalpha()).lower()
line_two = "".join(i for i in input() if i.isalpha()).lower()
i = 0
flag = True

while i <= min(len(line_one), len(line_two)) - 1:
    if line_one[i] == line_two[i]:
        i += 1
    else:
        flag = False
        break

if flag and len(line_one) == len(line_two):
    print("YES")
else:
    print("NO")