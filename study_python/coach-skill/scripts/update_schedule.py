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
  due    [--file path]                                темы к повторению
  stats  [--file path]                                сводка по темам

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

DEFAULT_FILE = "progress.json"
INTERVALS = [1, 3, 7, 14, 30]  # дни; после 30 — умножение на ease


def load(path: Path) -> dict:
    if not path.exists():
        return {"topics": {}}
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

    t["last_seen"] = date.today().isoformat()
    t["next_review"] = (
        date.today() + timedelta(days=t["interval_days"])
    ).isoformat()
    save(path, data)
    print(
        f"{topic}: grade={grade}, следующее повторение через "
        f"{t['interval_days']} дн. ({t['next_review']})"
    )


def due(path: Path) -> None:
    data = load(path)
    today = date.today().isoformat()
    rows = [
        (t["next_review"], avg(t["grades"]), name)
        for name, t in data["topics"].items()
        if t.get("next_review", "9999") <= today
    ]
    if not rows:
        print("Повторений на сегодня нет.")
        return
    # слабые (низкий средний grade) — первыми
    for next_review, mean, name in sorted(rows, key=lambda r: (r[1], r[0])):
        print(f"{name}  (средний grade {mean:.1f}, срок был {next_review})")


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
        print(
            f"{name}: попыток {t['attempts']}, средний grade "
            f"{avg(t['grades']):.1f}, последние {last5}, "
            f"повторение {t.get('next_review', '—')}"
        )


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=["record", "due", "stats"])
    p.add_argument("--topic")
    p.add_argument("--grade", type=int, choices=[1, 2, 3, 4, 5])
    p.add_argument("--file", default=DEFAULT_FILE)
    args = p.parse_args()

    path = Path(args.file)
    if args.command == "record":
        if not args.topic or args.grade is None:
            sys.exit("record требует --topic и --grade")
        record(path, args.topic, args.grade)
    elif args.command == "due":
        due(path)
    else:
        stats(path)


if __name__ == "__main__":
    main()
