"""
Задача: Искомый месяц

Напишите функцию get_month(language, number), которая принимает язык
('ru' или 'en') и номер месяца number (от 1 до 12 включительно) и
ВОЗВРАЩАЕТ название этого месяца на нужном языке.

Вход: два аргумента — language ('ru'/'en') и number (1..12), input() не нужен
Выход: функция ничего не печатает, а возвращает строку с названием месяца

Пример вызова:
print(get_month('ru', 1))
print(get_month('ru', 12))
print(get_month('en', 1))
print(get_month('en', 10))

Вывод:
"январь"
"декабрь"
"january"
"october"
# в файле образец в кавычках; печатать кавычки не нужно
"""


def get_month(language: str, number: int) -> str:
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
              'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']
    return lng_ru[number - 1] if language == "ru" else lng_en[number - 1]


language, number = input(), int(input())
print(get_month(language, number))
