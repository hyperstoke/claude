"""
Задача: «Negatives, Zeros and Positives»

На вход программе подаются натуральное число n, а затем n целых чисел.
Напишите программу, которая сначала выводит все отрицательные числа,
затем нули, а затем все положительные числа. Все числа должны быть
выведены в том же порядке, в котором они были введены, каждое на
отдельной строке.

Формат входных данных:
    Натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных:
    Текст в соответствии с условием задачи.
"""
count_value = int(input())
lst_value = []

for _ in range(count_value):
    lst_value.append(int(input()))

new_lst_value = []

for num in lst_value:
    if num < 0:
        new_lst_value.append(num)
for num in lst_value:
    if num == 0:
        new_lst_value.append(num)
for num in lst_value:
    if num > 0:
        new_lst_value.append(num)

print(* new_lst_value, sep="\n")


