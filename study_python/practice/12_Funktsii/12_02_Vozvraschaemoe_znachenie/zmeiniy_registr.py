'''
Змеиный регистр

Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента
строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно по ссылке.
Примечание 2.

Приведённый ниже код:
print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

должен выводить:
this_is_camel_cased
is_prime_number
'''


def convert_to_python_case(text):
    result = text[:1].lower()
    for char in text[1:]:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result


txt = input()

print(convert_to_python_case(txt))