# Нижний регистр
# На вход подаётся строка. Нужно посчитать количество буквенных
# символов в нижнем регистре и вывести это число.

text = input()

count = 0

for i in text:
    if i.islower():
        count += 1
print(count)

count = sum(1 for i in text if i.islower())

print(count)