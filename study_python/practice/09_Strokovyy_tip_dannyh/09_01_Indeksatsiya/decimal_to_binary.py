# Stepik 9.1 — "Decimal to Binary"
# Дано: натуральное число, записанное в десятичной системе счисления.
# Нужно: перевести и вывести это число в двоичной системе счисления.


num = int(input())
binary_num = []

while num > 0:
    modulo = num % 2
    binary_num.append(modulo)
    num = num // 2

if not binary_num:
    print(0)
else:
    print(*binary_num[::-1], sep="")
    print(*reversed(binary_num), sep="")

