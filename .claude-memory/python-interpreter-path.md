---
name: python-interpreter-path
description: "Как запускать Python в проекте: только python3, команды `python` в PATH нет; машина одна — MacBook"
metadata:
  node_type: memory
  type: reference
  originSessionId: bb5d3451-d1e7-4b92-9f52-a7b5ac18a590
  modified: 2026-09-08T21:06:03.069Z
---

Работа идёт только на MacBook — других машин у пользователя нет
(подтверждено 2026-09-09).

Рабочий интерпретатор — `python3`
(`/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`, 3.14.6).
Команды `python` в PATH **нет**, вызов без тройки падает. `uv` установлен
в `~/.local/bin/uv`.

Служебные скрипты проекта запускать из корня репозитория:
`python3 study_python/coach-skill/scripts/update_schedule.py due`.

До 2026-09-09 здесь была записана раскладка второго устройства (ПК с
Windows 11, интерпретатор внутри uv). Второго устройства нет — факт был
ошибочным. Связано с [[project-github-sync]].
