#!/usr/bin/env python3
"""Статистика и интервальное повторение (упрощённый SM-2).

Хранит всё в progress.json:
{
  "topics": {
    "методы строк": {
      "attempts": 4,
      "grades": [3, 4, 5, 5],
      "interval_days": 7,
      "ease": 2.5,
      "next_review": "2026-07-19",
      "last_seen": "2026-07-12"
    }
  }
}

Команды:
  record --topic "тема" --grade 1..5 [--file path]   записать результат
  due    [--limit N | --all] [--file path]           темы к повторению
  retire --topic "тема" --reason "..." [--file path] вывести тему из ротации
  stats  [--file path]                                сводка по темам

`due` по умолчанию показывает 3 самые слабые темы и счётчик остальных:
список из десятка тем ученик не разбирает, он его игнорирует.

`retire` — аналог «снятия по давности» из practice_queue: тема освоена и
раздел курса закрыт, держать её в ротации незачем. Требует причины, запись
остаётся в файле с пометкой, ничего не удаляется.

Шкала grade (описывает всю сессию, а не последнюю версию кода; подходят
несколько — брать меньшую):
1 — примеры не прошли; 2 — решено, но понадобились содержательные подсказки;
3 — работает, но неоптимально; 4 — оптимально, были замечания на ревью;
5 — чисто: первая присланная версия прошла и оптимальна.
"""

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

# Путь считается от самого скрипта, а не от текущей папки: скрипт запускают
# из корня репозитория, и относительный "progress.json" там не находился —
# load() молча возвращал пустой словарь, due печатал «повторений нет», а
# record создавал второй файл рядом. Найдено 2026-08-27.
DEFAULT_FILE = Path(__file__).resolve().parents[2] / "coach" / "progress.json"
INTERVALS = [1, 3, 7, 14, 30]  # дни; после 30 — умножение на ease


def load(path: Path) -> dict:
    if not path.exists():
        sys.exit(
            f"Файл прогресса не найден: {path}\n"
            "Если это первый запуск — создать его содержимым {\"topics\": {}}."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def record(path: Path, topic: str, grade: int) -> None:
    data = load(path)
    t = data["topics"].setdefault(
        topic,
        {"attempts": 0, "grades": [], "interval_days": 0, "ease": 2.5},
    )
    t["attempts"] += 1
    t["grades"].append(grade)
    t["grades"] = t["grades"][-20:]  # хранить хвост, не всю историю

    # SM-2 упрощённо: провал/неоптимально сбрасывает интервал,
    # успех двигает по лестнице INTERVALS, дальше — ease-множитель.
    if grade <= 3:
        t["interval_days"] = 1 if grade <= 1 else 3
        t["ease"] = max(1.3, t["ease"] - 0.2)
    else:
        t["ease"] = min(2.8, t["ease"] + (0.1 if grade == 5 else 0.0))
        cur = t["interval_days"]
        nxt = next((i for i in INTERVALS if i > cur), None)
        t["interval_days"] = (
            nxt if nxt is not None else round(cur * t["ease"])
        )

    t.pop("retired", None)  # новая оценка возвращает тему в ротацию
    t["last_seen"] = date.today().isoformat()
    t["next_review"] = (
        date.today() + timedelta(days=t["interval_days"])
    ).isoformat()
    save(path, data)
    print(
        f"{topic}: grade={grade}, следующее повторение через "
        f"{t['interval_days']} дн. ({t['next_review']})"
    )


def due(path: Path, limit: int | None) -> None:
    data = load(path)
    today = date.today().isoformat()
    rows = [
        (t["next_review"], avg(t["grades"]), name)
        for name, t in data["topics"].items()
        if t.get("next_review", "9999") <= today and not t.get("retired")
    ]
    if not rows:
        print("Повторений на сегодня нет.")
        return
    # слабые (низкий средний grade) — первыми
    rows.sort(key=lambda r: (r[1], r[0]))
    shown = rows if limit is None else rows[:limit]
    for next_review, mean, name in shown:
        print(f"{name}  (средний grade {mean:.1f}, срок был {next_review})")
    hidden = len(rows) - len(shown)
    if hidden:
        print(
            f"\n…и ещё {hidden} тем(ы) просрочено. Весь список: due --all.\n"
            "Если список не тает неделями — это не повод его листать, "
            "а повод разобрать пару тем или снять освоенные через retire."
        )


def retire(path: Path, topic: str, reason: str) -> None:
    data = load(path)
    t = data["topics"].get(topic)
    if t is None:
        sys.exit(f"Темы нет в progress.json: {topic}")
    if t.get("retired"):
        sys.exit(f"Тема уже снята {t['retired']['date']}: {t['retired']['reason']}")
    t["retired"] = {"date": date.today().isoformat(), "reason": reason}
    save(path, data)
    print(f"{topic}: снята с ротации — {reason}")
    print("Вернуть в ротацию — record с новой оценкой.")


def avg(grades: list) -> float:
    return sum(grades) / len(grades) if grades else 0.0


def stats(path: Path) -> None:
    data = load(path)
    if not data["topics"]:
        print("Статистики пока нет.")
        return
    for name, t in sorted(
        data["topics"].items(), key=lambda kv: avg(kv[1]["grades"])
    ):
        last5 = t["grades"][-5:]
        mark = f" [снята {t['retired']['date']}]" if t.get("retired") else ""
        print(
            f"{name}: попыток {t['attempts']}, средний grade "
            f"{avg(t['grades']):.1f}, последние {last5}, "
            f"повторение {t.get('next_review', '—')}{mark}"
        )


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=["record", "due", "retire", "stats"])
    p.add_argument("--topic")
    p.add_argument("--grade", type=int, choices=[1, 2, 3, 4, 5])
    p.add_argument("--reason")
    p.add_argument("--limit", type=int, default=3)
    p.add_argument("--all", action="store_true", help="показать все просроченные")
    p.add_argument("--file", default=DEFAULT_FILE)
    args = p.parse_args()

    path = Path(args.file)
    if args.command == "record":
        if not args.topic or args.grade is None:
            sys.exit("record требует --topic и --grade")
        record(path, args.topic, args.grade)
    elif args.command == "due":
        due(path, None if args.all else args.limit)
    elif args.command == "retire":
        if not args.topic or not args.reason:
            sys.exit("retire требует --topic и --reason")
        retire(path, args.topic, args.reason)
    else:
        stats(path)


if __name__ == "__main__":
    main()
