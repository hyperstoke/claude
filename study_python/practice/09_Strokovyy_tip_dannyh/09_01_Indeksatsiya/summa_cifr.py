# Stepik 9.1 — "Цифра 1"
# Дано: строка, состоящая из цифр.
# Нужно: посчитать и вывести сумму цифр этой строки.


num = input()
sum_num = 0

for digit in num:
    sum_num += int(digit)

print(sum_num)