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
- **Пополнять кит можно и нужно.** Новые фото → `assets/bitrix24-images/people/`,
  иконки → `assets/bitrix24-images/icons/`, логотипы → `assets/bitrix24-logo/`.
  После добавления зарегистрируй ассет в `DESIGN_SYSTEM.md` / `SKILL.md`, чтобы
  скилл о нём знал. Именуй как существующие файлы.
- **Не коммить сгенерированные выгрузки** — готовые `guide.pdf`, слайды
  `slide-01.png` и прочие результаты рендера под конкретную задачу. Это НЕ то же,
  что новые ассеты кита (их добавлять нужно) — речь про финальные выгрузки.
- **Ассеты не публикуем вовне** (не выкладывать наружу, не делать репо
  публичным) — это внутренние материалы Bitrix24 Partners. Внутри репо
  пополнять кит — пожалуйста.
- Один PR = одно логическое изменение. Так проще ревьюить и откатывать.
