# Первое и последнее вхождение
#
# На вход программе подаётся строка текста. Если в этой строке буква «f»
# встречается только один раз, выведите её индекс. Если она встречается
# два и более раза, выведите индексы её первого и последнего вхождения
# на одной строке, разделённые символом пробела. Если буква «f» в данной
# строке не встречается, следует вывести «NO» (без кавычек).
#
# Формат входных данных: строка текста.
# Формат выходных данных: индекс(ы) вхождения буквы «f» или «NO».

#fist_second_index = []
#start_index = 0
#
#for i in text:
#    if i == "f":
#        fist_second_index.append(start_index) # type: ignore
#    start_index += 1
#if len(fist_second_index) == 0: # type: ignore
#    print("NO")
#elif len(fist_second_index) == 1: # type: ignore
#    print(*fist_second_index) # type: ignore
#else:
#    print(fist_second_index[0], fist_second_index[-1]) # type: ignore


text = input()

count = text.count("f")

if count == 0:
    print("NO")
elif count == 1:
    print(text.find("f"))
else:
    print(text.find("f"), text.rfind("f"))