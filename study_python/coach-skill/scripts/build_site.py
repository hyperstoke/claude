#!/usr/bin/env python3
"""Сборка сайта прогресса: данные из coach/ → константы в roadmap_artifact.html.

Убирает ручное дублирование JSON в HTML и вшивает код решённых задач
(опубликованный артефакт на claude.ai не имеет доступа к локальным файлам,
поэтому код должен лежать прямо в странице).

Что делает:
  1. Читает coach/activity.json и coach/practice_queue.json.
  2. Для каждого item с полем file читает .py-файл, кладёт его текст в
     item.code и ссылку на GitHub в item.github.
  3. Генерирует JS-константы TRACKING_SINCE, ACTIVITY, DEADLINE,
     PRACTICE_QUEUE и вставляет их в roadmap_artifact.html между маркерами
     /* @gen:start ... */ и /* @gen:end */.

Запуск (рабочий Python через uv на ПК):
  <uv-python> study_python/coach-skill/scripts/build_site.py

После сборки — передеплоить артефакт на тот же URL и (при обычном пуше)
выгрузить на GitHub. Дневные пуши так несут актуальный прогресс.
"""

import json
import re
import sys
from pathlib import Path

# Консоль на ПК — cp1251; выводим в UTF-8, чтобы не падать на «→» и кириллице.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

REPO_ROOT = Path(__file__).resolve().parents[3]
ACTIVITY_JSON = REPO_ROOT / "study_python" / "coach" / "activity.json"
QUEUE_JSON = REPO_ROOT / "study_python" / "coach" / "practice_queue.json"
HTML = REPO_ROOT / "study_python" / "roadmap_artifact.html"
GITHUB_BASE = "https://github.com/hyperstoke/claude/blob/main/"

START = "/* @gen:start"
END = "/* @gen:end */"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def embed_file(entry: dict, rel: str, where: str, warnings: list[str]) -> bool:
    """Вшить в entry поля file/code/github по пути rel (от корня репо).

    Возвращает True, если файл найден и код вшит. Пустой code=None + warning,
    если файла нет — страница покажет «код не сохранён».
    """
    entry["file"] = rel
    fpath = REPO_ROOT / rel
    if fpath.exists():
        entry["code"] = fpath.read_text(encoding="utf-8")
        entry["github"] = GITHUB_BASE + rel
        return True
    warnings.append(f"{where}: файл не найден — {rel}")
    entry["code"] = None
    return False


def enrich_items(activity: dict) -> tuple[dict, int, list[str]]:
    """Вернуть {дата: день} с вшитым кодом, число вшитых файлов и предупреждения."""
    days = {}
    embedded = 0
    warnings: list[str] = []
    for date, day in activity["days"].items():
        items = []
        for it in day.get("items", []):
            entry = {"name": it["name"], "kind": it.get("kind", "пройдено")}
            rel = it.get("file")
            if rel and embed_file(entry, rel, date, warnings):
                embedded += 1
            items.append(entry)
        days[date] = {
            "level": day["level"],
            "tasks": day["tasks"],
            "note": day["note"],
            "items": items,
        }
    return days, embedded, warnings


def js_const(name: str, value) -> str:
    # json.dumps даёт валидный JS-литерал; экранируем закрывающий тег,
    # чтобы код с "</script>" внутри строки не рвал разметку.
    dumped = json.dumps(value, ensure_ascii=False, indent=2)
    dumped = dumped.replace("</", "<\\/")
    return f"  const {name} = {dumped};\n"


def build_block(activity: dict, queue: dict) -> str:
    days, embedded, warnings = enrich_items(activity)
    pq = []
    for e in queue.get("queue", []):
        entry = {
            "topic": e["topic"],
            "reason": e["reason"],
            "difficulty": e["difficulty"],
            "status": e["status"],
        }
        rel = e.get("file")
        if rel and embed_file(entry, rel, f"queue/{e.get('id', '?')}", warnings):
            embedded += 1
        pq.append(entry)
    dl = activity["deadline"]
    deadline = {
        "goal": dl["goal"],
        "date": dl["date"],
        "note": dl.get("note") or dl.get("basis", ""),
    }
    progress = activity.get("progress")
    if isinstance(progress, dict):
        progress = {k: v for k, v in progress.items() if not k.startswith("_")}
    block = (
        f"  {START} — генерируется scripts/build_site.py из coach/*.json, вручную не править */\n"
        + js_const("TRACKING_SINCE", activity["tracking_since"])
        + js_const("ACTIVITY", days)
        + js_const("DEADLINE", deadline)
        + js_const("PROGRESS", progress)
        + js_const("PRACTICE_QUEUE", pq)
        + f"  {END}"
    )
    return block, embedded, warnings


def main() -> None:
    activity = load_json(ACTIVITY_JSON)
    queue = load_json(QUEUE_JSON)
    block, embedded, warnings = build_block(activity, queue)

    html = HTML.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END), re.DOTALL
    )
    if not pattern.search(html):
        sys.exit(
            "Не найдены маркеры /* @gen:start ... @gen:end */ в "
            f"{HTML.name} — добавь их вокруг блока констант."
        )
    html = pattern.sub(lambda _: block, html, count=1)
    HTML.write_text(html, encoding="utf-8")

    for w in warnings:
        print("  ! " + w)
    n_days = len(activity["days"])
    print(f"OK: {n_days} дней, вшито файлов кода: {embedded} → {HTML.name}")


if __name__ == "__main__":
    main()
