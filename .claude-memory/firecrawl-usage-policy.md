---
name: firecrawl-usage-policy
description: "Firecrawl CLI установлен (ПК, 2026-07-15); использовать только для нестабильных фактов, через research-skill с кэшем"
metadata: 
  node_type: memory
  type: project
  originSessionId: 04e85b60-d3f5-4b4b-9824-2c1d7aa8a833
---

2026-07-15 в проект `claude/` интегрирован Firecrawl CLI (v1.19.26,
npm-пакет `firecrawl-cli`). На ПК (Windows) установлен Node.js v24.18.0
portable в `%LOCALAPPDATA%\Programs\nodejs` (winget сломан — источник
требует админ-прав на починку). Ключ — в user-переменной окружения
`FIRECRAWL_API_KEY`. На Mac CLI ещё НЕ установлен — поставить при первой
необходимости (`npm install -g firecrawl-cli` + тот же ключ).

**Политика:** Firecrawl — только для нестабильных фактов (тренды,
вакансии, релизы, выбор актуальных материалов), только после проверки
локальных файлов, памяти и кэша `study_python/research/INDEX.md`.
Правила и иерархия инструментов — в `study_python/research-skill/SKILL.md`
и в корневом CLAUDE.md проекта (раздел «Источники информации»).
Ежедневная работа coach-skill (задачи, проверка, статистика) — полностью
локальная, без интернета. См. [[python-interpreter-path]].
