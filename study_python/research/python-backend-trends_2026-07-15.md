# Тренды Python-backend — исследование 2026-07-15

Первый запуск режима 4 coach-skill (тестовый прогон интеграции Firecrawl).
TTL: 30 дней. Инструменты: Firecrawl `search` (4 запроса, --tbs qdr:y)
+ точечный `scrape` двух источников.

## Запросы

- `Python backend best practices 2026`
- `Python idiomatic code style 2026 typing pathlib`
- `Python backend разработчик вакансии требования 2026` (--location Russia)
- `Python tooling 2026 uv ruff`

## Источники

- https://rollbar.com/blog/python-backend-frameworks/ — гайд по выбору
  фреймворка 2026 (скрейплен, выжимка ниже).
- https://ru.hexlet.io/blog/posts/kak-stat-python-razrabotchikom-2026 —
  джуниорский стек РФ 2026 (скрейплен, выжимка ниже).
- https://hh.ru/vacancy/128750255 — реальная вакансия «Стажёр/Backend
  Python»: Python + БД-библиотеки (psycopg, clickhouse), FastAPI,
  базовый SQL (сниппет из поиска).
- https://www.kdnuggets.com/python-project-setup-2026-uv-ruff-ty-polars —
  сетап 2026: uv + Ruff (+ Ty как типчекер) (сниппет).
- https://medium.com/the-pythonworld/my-entire-python-development-setup-in-2026-every-tool-listed-4f41561e82e6 —
  uv заменяет pip/pip-tools/virtualenv/pyenv; FastAPI — выбор по
  умолчанию для новых backend-сервисов (сниппет).

## Выжимка

**Фреймворки (rollbar, 2026).** Доминируют трое: Django, FastAPI, Flask.
FastAPI — для современных REST API и микросервисов; Django — для
полнофункциональных приложений (админка, безопасность, документация);
Flask — прототипы и максимальная гибкость. Для новичков rollbar называет
входными Flask/Django, но FastAPI — «для тех, кто дружит с тайп-хинтами
и async» — что совпадает с нашим roadmap (FastAPI первым, Django вторым).

**Рынок РФ.** Реальная стажёрская вакансия просит: Python, библиотеки БД
(psycopg, clickhouse), FastAPI, базовый SQL. Подтверждает порядок этапов
roadmap: SQL перед фреймворком, FastAPI как первый фреймворк.

**Инструменты.** Консенсус 2026: uv (пакеты/окружения, вместо
pip/virtualenv/pyenv) + Ruff (линтер/форматтер, вместо flake8/black).
Появляется Ty (типчекер от Astral) — пока «на горизонте». У ученика uv
уже стоит (Python на ПК установлен через uv) — попадание в тренд.

**Идиоматика.** Стабильный набор: тайп-хинты, f-строки, pathlib,
dataclasses — ничего революционного за год; для текущего этапа (строки)
изменений нет.

## Примечание

Статья hexlet.io при скрейпе отдавалась медленно (первый заход упал по
таймауту); её вклад в выжимку — из поискового сниппета: «какой стек
просят на джуниорских вакансиях 2026». При следующем анализе можно
дожать `scrape --wait-for 3000 --max-age`.
