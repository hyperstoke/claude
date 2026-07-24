"""
Задача: «Порядок книг»

Все книги в домашней библиотеке должны быть отсортированы по возрастанию:
сначала по фамилиям авторов, а при совпадении фамилий — по названиям
книг. Напишите программу, которая проверяет, верно ли отсортированы
книги.

Каждая книга задаётся строкой в формате:
    <фамилия автора> <инициалы автора>, «<название книги>»

Программа должна вывести "YES", если книги отсортированы по правилам,
иначе "NO".

Формат входных данных:
    Число n, затем n строк — описания книг в указанном формате.

Формат выходных данных:
    "YES" или "NO" в соответствии с условием задачи.

Примечание 1. Инициалы автора при сортировке не учитываются.
Примечание 2. Книги в наборе не повторяются.
Примечание 3. Фамилия автора состоит из одного слова.

Примечание. Пример теста:
    2
    "During A.B., «Заводной апельсин»"
    "Orwell G., «1984»"
    -> "YES"
"""


count_books = int(input())
books = []
flag = True

for _ in range(count_books):
    books.append(input())

for i in range(len(books) - 1):
    start_surname_one = books[i].find(" ")
    surname_one = books[i][:start_surname_one]

    start_surname_two = books[i + 1].find(" ")
    surname_two = books[i + 1][:start_surname_two]

    if surname_one < surname_two:
        i += 1
    elif surname_one == surname_two:
        start_title_one = books[i].find("«")
        title_one = books[i][start_title_one +1: -1]

        start_title_two = books[i + 1].find("«")
        title_two = books[i + 1][start_title_two +1: -1]

        if title_one > title_two:
            flag = False
            break
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")