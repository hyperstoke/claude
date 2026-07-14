# Задача: is_palindrome_query
# Тема: методы строк (lower, replace, срез s[::-1])  |  Сложность: 1
#
# Легенда: поисковый движок блога дедуплицирует запросы пользователей —
# если запрос является палиндромом (без учёта пробелов и регистра), его
# помечают как "palindrome" для отдельной статистики, иначе — "not palindrome".
#
# Вход:  строка запроса через input() (могут быть пробелы, любой регистр).
# Выход: print "palindrome" или "not palindrome".
#
# Примеры:
#   "A man a plan a canal Panama" -> palindrome
#   "hello world"                 -> not palindrome
#   "Was it a car or a cat I saw" -> palindrome
#   ""                             -> palindrome


text = input()

text = text.lower()
text = text.replace(" ", "")

if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")