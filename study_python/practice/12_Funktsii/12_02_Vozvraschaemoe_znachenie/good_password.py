"""
Good password

Напишите функцию is_password_good(password), которая принимает в качестве
аргумента строковое значение пароля password и возвращает значение True,
если пароль является надёжным, или False в противном случае.

Пароль является надёжным, если:
- его длина не менее 8 символов;
- он содержит как минимум одну заглавную букву (верхний регистр);
- он содержит как минимум одну строчную букву (нижний регистр);
- он содержит хотя бы одну цифру.

Примечание. Приведённый ниже код:
print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

должен выводить:
True     # длина 10, есть C, есть a, есть 1
False    # длина 6 — коротко
"""


def is_password_good(password: str) -> bool:
    return all([len(password) >= 8,
                any(ch.isupper() for ch in password),
                any(ch.islower() for ch in password),
                any(ch.isdigit() for ch in password)])


pas = input()


print(is_password_good(pas))

