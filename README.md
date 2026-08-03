# Bitrix24 Partner Brand Style — Claude Code skill

Официальный партнёрский фирстиль Bitrix24 как one-prompt генератор контента для
Claude Code. Скилл собирает A4-PDF, LinkedIn-карусели и Instagram Stories из
встроенного бренд-кита (шрифт Montserrat, логотипы, цвета, компоненты, фото
людей, иконки).

Полное описание возможностей — в [`SKILL.md`](SKILL.md), сценарии
использования — в [`USAGE_GUIDE.md`](USAGE_GUIDE.md), требования к окружению —
в [`INSTALL.md`](INSTALL.md).

> ⚠️ **Private / internal.** Репозиторий содержит фирменные ассеты Bitrix24
> Partners (логотипы, шрифты, фото людей). Не делать публичным, не выкладывать
> ассеты вовне.

---

## Установка через git (рекомендуемый способ)

Клонируй репозиторий **прямо в папку скиллов** Claude Code — тогда рабочая копия
и есть установленный скилл, а обновление сводится к `git pull`.

```bash
# личный скилл (доступен во всех проектах)
git clone <REPO_URL> ~/.claude/skills/bitrix24-partner-style
```

Проверь, что Claude Code видит скилл: в новой сессии он появится в списке как
`bitrix24-partner-style`.

Требования к окружению (Chrome, Python 3, PyMuPDF/poppler) — см.
[`INSTALL.md`](INSTALL.md).

## Обновиться до свежей версии

```bash
cd ~/.claude/skills/bitrix24-partner-style
git pull
```

## Внести изменения

Правки принимаются **через Pull Request** — см. [`CONTRIBUTING.md`](CONTRIBUTING.md).
