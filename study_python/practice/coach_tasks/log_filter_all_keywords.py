"""
Задача: Поиск по логу сервиса
Тема: проверка нескольких условий сразу через all()  |  Сложность: 5 (средняя)

Легенда: на бэкенде сервиса включили простой поиск по логам — примерно то,
что делают Kibana или `grep` с несколькими терминами. Дежурный инженер вводит
несколько ключевых слов, и система показывает только те строки лога, где
встречаются ВСЕ введённые слова сразу. Регистр значения не имеет: инженер в
три часа ночи пишет "error", а в логе может стоять "ERROR".

Вход:  натуральное число n — количество строк лога;
затем n строк лога;
затем одна строка с ключевыми словами, разделёнными пробелом.
Выход: строки лога, содержащие все ключевые слова, каждая на отдельной
строке, в исходном порядке и в исходном виде (регистр не менять).
Если не подошла ни одна строка — вывести "Совпадений нет".

Примеры:
    4
    2026-08-04 ERROR payment gateway timeout
    2026-08-04 INFO payment accepted
    2026-08-04 error DB connection lost
    2026-08-04 WARN payment retry scheduled
    error payment
    -> 2026-08-04 ERROR payment gateway timeout
    # только здесь есть и "error", и "payment"; регистр в логе другой

    3
    GET /api/orders 200
    POST /api/orders 500
    GET /api/users 200
    api 200
    -> GET /api/orders 200
GET /api/users 200
    # оба слова встречаются, порядок строк сохранён

    2
    INFO cache warm
    INFO cache cold
    redis
    -> Совпадений нет   # граничный случай: не подошла ни одна строка
"""

# твой код здесь

count_logs = int(input())

logs = [input() for _ in range(count_logs)]
correct_logs = []

triggers = input().split()

for log in logs:
    if all(trigger.lower() in log.lower() for trigger in triggers):
        correct_logs.append(log)

if len(correct_logs) > 0:
    print(*correct_logs, sep="\n")
else:
    print("Совпадений нет")