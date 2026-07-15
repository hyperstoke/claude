---
name: mac-node-firecrawl
description: На Mac node и firecrawl CLI поставлены вручную в ~/.local/nodejs; ключ Firecrawl в ~/.zshrc
metadata: 
  node_type: memory
  type: project
  originSessionId: e0caa131-459d-4f23-b570-74233c348cd8
---

На Mac (arm64) **нет Homebrew**. Node.js установлен вручную как официальный
бинарник в `~/.local/nodejs` (LTS v24, 2026-07-15), PATH прописан в `~/.zshrc`.
`firecrawl-cli` установлен глобально через этот node (`npm install -g`,
prefix = `~/.local/nodejs`, sudo не нужен). `FIRECRAWL_API_KEY` — тоже в
`~/.zshrc` (значение не хранить здесь и не коммитить). В неинтерактивном
Bash-tool профиль не подхватывается — при запуске node/firecrawl вручную
добавлять `export PATH="$HOME/.local/nodejs/bin:$PATH"`.

Связано с [[github-sync]] (gh в `~/.local/bin`, тоже добавлен в PATH в ~/.zshrc).
