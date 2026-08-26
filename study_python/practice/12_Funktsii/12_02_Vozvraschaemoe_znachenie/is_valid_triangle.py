"""
Задача: Is the Triangle Valid?

Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает
три натуральных числа — длины сторон, — и ВОЗВРАЩАЕТ True, если невырожденный
треугольник с такими сторонами существует, или False в противном случае.

Вход: три аргумента — числа side1, side2, side3
Выход: функция ничего не печатает, а возвращает True или False
Числа вводятся с клавиатуры, по одному в строке, и передаются в функцию

Примечание: с этой задачей мы уже сталкивались при изучении условного оператора.

Пример вызова:
print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))

Вывод:
"True"
"False"
"True"
# в файле образец показан в кавычках; печатать кавычки не нужно
# 2, 3, 10 — треугольника нет: 2 + 3 меньше 10
"""


def is_valid_triangle(side1, side2, side3):
    return (side1 + side2 > side3
        and side1 + side3 > side2
        and side2 + side3 > side1)


a, b, c = int(input()), int(input()), int(input())


print(is_valid_triangle(a, b, c))