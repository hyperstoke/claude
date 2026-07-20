---
name: python-interpreter-path
description: "Где на ПК (Windows) лежит рабочий Python — системный `python` не работает"
metadata: 
  node_type: memory
  type: reference
  originSessionId: bb5d3451-d1e7-4b92-9f52-a7b5ac18a590
---

На ПК пользователя (Windows 11) команда `python` в PATH — это Store-заглушка
Microsoft, которая падает с «Python was not found». `py` launcher тоже нет.

Рабочий интерпретатор (через uv):
`C:\Users\Admin\AppData\Roaming\uv\python\cpython-3.14.4-windows-x86_64-none\python.exe`

Использовать полный путь, когда нужно запустить Python-скрипт из Bash/PowerShell
для служебных задач. Связано с [[chatgpt-export-processed]].
