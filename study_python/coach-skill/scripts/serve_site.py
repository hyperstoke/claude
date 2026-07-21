#!/usr/bin/env python3
"""Локальный предпросмотр сайта прогресса (roadmap_artifact.html).

Стандартный `python -m http.server` отдаёт HTML без charset, и браузер
ломает кириллицу: у файла-артефакта нет своего <head> с <meta charset> —
его добавляет скелет claude.ai при публикации. Поэтому здесь тот же
сервер, но с явным UTF-8 в Content-Type для .html.

Запуск (рабочий Python через uv на ПК):
  <uv-python> study_python/coach-skill/scripts/serve_site.py [порт]

Страница: http://127.0.0.1:8737/roadmap_artifact.html
"""

import functools
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parents[2]  # study_python/
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8737

if __name__ == "__main__":
    SimpleHTTPRequestHandler.extensions_map[".html"] = "text/html; charset=utf-8"
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(SITE_DIR))
    with ThreadingHTTPServer(("127.0.0.1", PORT), handler) as srv:
        print(f"serving {SITE_DIR} at http://127.0.0.1:{PORT}")
        srv.serve_forever()
