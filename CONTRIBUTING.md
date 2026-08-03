# Как вносить изменения в скилл

Работаем через **Pull Request**. По договорённости **не пушим в `main`
напрямую** — все изменения идут веткой и через PR, чтобы владелец репозитория
отревьюил, что попадает в общий скилл. (Технической блокировки нет — это
командное соглашение, соблюдаем его сознательно.)

## Разовая настройка

```bash
# 1. Убедись, что git знает, кто ты
git config --global user.name "Имя Фамилия"
git config --global user.email "you@example.com"

# 2. Клонируй репозиторий в папку скиллов (если ещё не сделал)
git clone https://github.com/rabenok2105/bitrix24-partner-style.git ~/.claude/skills/bitrix24-partner-style
cd ~/.claude/skills/bitrix24-partner-style
```

## Цикл внесения правки

```bash
# всегда стартуй от свежего main
git checkout main
git pull

# заведи ветку под задачу
git checkout -b feature/kratkoe-opisanie

# ...правишь SKILL.md / assets / scripts...

git add -A
git commit -m "Что изменил и зачем"
git push -u origin feature/kratkoe-opisanie
```

Дальше открой Pull Request на GitHub (или командой):

```bash
gh pr create --fill
```

После ревью и мержа — обнови свою копию:

```bash
git checkout main && git pull
```

## Что важно помнить

- **Меняешь стиль → правь `assets/` и `SKILL.md` вместе.** Скилл читает правила
  из `SKILL.md`, а верстку берёт из `assets/` (`bitrix24-kit.css`,
  `bitrix24-template.html`, `DESIGN_SYSTEM.md`).
- **Не коммить сгенерированные файлы** (готовые PDF/PNG выгрузки) — они в
  `.gitignore`. В репозитории — только исходники скилла и бренд-кит.
- **Ассеты не публикуем вовне** — репозиторий private, это внутренние
  материалы Bitrix24 Partners.
- Один PR = одно логическое изменение. Так проще ревьюить и откатывать.
