# Оркестрация субагентов — гайдлайны Anthropic

Поисковый запрос: правила оркестрации субагентов в Claude Code (когда
нужен субагент, как ставить задание, экономика моделей, частые ошибки).

Источники:
- https://www.anthropic.com/engineering/building-effective-agents
- https://www.anthropic.com/engineering/multi-agent-research-system
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/costs
- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/model-config

## Выжимка

**Паттерны и когда агент вообще не нужен.** Из building-effective-agents:
orchestrator-workers — когда подзадачи нельзя предсказать заранее; routing —
чёткая классификация входов, в том числе по размеру модели; parallelization —
sectioning (разбить на независимые куски) или voting (несколько прогонов на
согласованность); evaluator-optimizer — когда есть чёткие критерии и итерации
дают измеримый прирост. Первый шаг всегда — проверить, не хватит ли одного
вызова модели: «optimizing single LLM calls… is usually enough».

**Как ставить задание субагенту.** «Each subagent needs an objective, an
output format, guidance on the tools and sources to use, and clear task
boundaries» (multi-agent-research-system). Масштаб по сложности задачи:
«Simple fact-finding requires just 1 agent with 3-10 tool calls, direct
comparisons might need 2-4 subagents… complex research might use more than
10 subagents».

**Экономика.** В тестах Anthropic связка Opus 4 (лид) + Sonnet 4 (субагенты)
превзошла одиночный Opus 4 на 90.2% (multi-agent-research-system). Из
costs: «Sonnet handles most coding tasks well… Reserve Opus for complex
architectural decisions… For simple subagent tasks, specify model: haiku».
Изоляция контекста: «Delegate verbose operations to subagents so the
verbose output stays in the subagent's context while only a summary
returns» — сырые логи и файлы не должны попадать в основной контекст.
Субагенты не оправданы, когда: диалог частый и живой, нужен общий контекст
между фазами, правка точечная и быстрая, или критична задержка (лишний
раунд координации того не стоит).

**Механика Claude Code.** Frontmatter субагента: `model:` — `sonnet` /
`opus` / `haiku` / `inherit` или полный ID модели; порядок приоритета —
параметр `model` при вызове агента → frontmatter субагента →
`CLAUDE_CODE_SUBAGENT_MODEL` → модель текущей сессии (model-config,
sub-agents). `tools:` — allowlist разрешённых инструментов,
`disallowedTools:` — denylist. Описания субагентов должны быть короткими
(суммарно рекомендуется держать под ~15k токенов на все описания в
проекте). Субагент получает только свой системный промпт + CLAUDE.md
проекта + окружение — истории диалога с пользователем у него нет.

**Частые ошибки (best-practices, multi-agent-research-system).**
Дублирование работы из-за размытых, пересекающихся заданий; запуск
десятков субагентов на простые запросы («spawning 50 subagents for simple
queries»); one big kitchen-sink session вместо разделения по зонам;
повторные исправления одного и того же места в засорённом контексте — после
двух неудачных попыток лучше `/clear` и переформулировать задачу заново, а
не продолжать в том же контексте; над-специфицированный CLAUDE.md, который
глушит суть инструкций деталями; разрыв «доверяй, но проверяй» — «If you
can't verify it, don't ship it»; неограниченные задания вида «исследуй X»
без границ и критерия готовности; command-агенты (agent teams) обходятся
на порядок дороже одиночных субагентов (~7x токенов в измерениях
Anthropic) — по умолчанию использовать subagents, а не команды агентов.

## Чек-лист оркестрации (перенесён в корневой CLAUDE.md, раздел
«Оркестрация: дорогая модель делегирует»)

1. Сначала спросить: нужен ли субагент вообще, или хватит прямой правки.
2. Масштаб по сложности: один факт — один агент; аудит/сравнение — 2–4;
   не плодить агентов на простые запросы.
3. В задании субагенту — цель, формат вывода, границы (что НЕ трогать),
   файлы и источники, критерий готовности.
4. Зоны файлов не пересекаются между параллельными агентами.
5. В основной контекст — summary с фактами и цифрами, не сырые файлы и
   логи.
6. Проверка — отдельным reviewer с чистым контекстом, по критериям, а не
   по стилю.
7. Две неудачные попытки исправить одно и то же — стоп и
   переформулировка, а не докручивание в засорённом контексте.
8. Кэш исследований и правила источников действуют и для субагентов.
9. Ограничивать `tools` субагента тем, что реально нужно для его роли
   (allowlist во frontmatter), а не давать полный доступ по умолчанию.
10. Верификация — свежим субагентом без контекста автора правки, не тем
    же самым, что её делал.
11. Конкретные формулировки задания вместо расплывчатых («улучши код» →
    что именно улучшить, по каким критериям, в каких границах).
12. Command/agent-teams — дорогой паттерн (~7x токенов); по умолчанию
    обычные subagents.
