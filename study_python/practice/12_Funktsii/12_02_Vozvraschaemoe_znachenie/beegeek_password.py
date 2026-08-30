"""
BEEGEEK

BEEGEEK наконец-то открыл свой банк, в котором используются специальные
банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c —
натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики,
то он решил:
- число a должно быть палиндромом;
- число b должно быть простым;
- число c должно быть чётным.

Напишите функцию is_valid_password(password), которая принимает в качестве
аргумента строковое значение пароля password и возвращает значение True,
если пароль является действительным паролем BEEGEEK банка, или False
в противном случае.

Примечание. Приведённый ниже код:
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:
True     # 1221 палиндром, 101 простое, 22 чётное
False    # 30 не простое
False    # 112 не палиндром, 9 нечётное
False    # частей четыре, а не три
"""


def is_prime(num: int) -> bool:
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))


def is_valid_password(password: str) -> bool:
    parts = password.split(":")
    if (len(parts) != 3
            or not all(part.isdigit() and int(part) > 0 for part in parts)):
        return False

    a, b, c = parts
    return (a == a[::-1]
            and int(c) % 2 == 0
            and is_prime(int(b)))


text = input()


print(is_valid_password(text))