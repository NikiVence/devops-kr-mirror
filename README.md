# DevOps — контрольная работа №1 (ПР4)

Алиев Никита Денисович, ЭФБО-01-24. Инструменты DevOps, 2026.

Исходный проект преподавателя:
https://gitverse.ru/dgimatdinov/devops-kr-template.
У исходника основная ветка называется `master`; в учебной копии используется `main`.

## Реализовано

- `validate_email(email)` — проверка email из шаблона.
- `validate_phone(phone)` — российский номер: необязательный `+`, затем `7`
  и десять ASCII-цифр; пробелы и дефисы разрешены. Начало `8` отклоняется.
- `validate_snils(snils)` — сохранённая функция преподавателя с контрольной суммой.
- 15 тестов проверяют корректные и некорректные значения.

Пример преподавателя `001-001-999 32` исправлен в тесте на `001-001-999 65`:
взвешенная сумма цифр равна 65. Реализация СНИЛС при разрешении конфликта сохранена.

## Проверка

Из этой папки в текущем рабочем окружении:

```powershell
..\.venv\Scripts\python.exe -m pytest -v
```

После отдельного клонирования:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -v
```

## История задания

Выполнены четыре исходных коммита, настоящий interactive rebase с fixup/drop,
удаление WIP-заготовки `validate_inn` и разрешение конфликта с веткой преподавателя.
Обе функции, phone и snils, сохранены. До и после преобразований остались
теги `evidence/kr-dirty`, `evidence/kr-clean`, `evidence/kr-original`.

Протоколы: `reports/pr4/`. Отчёт: `reports/report_pr4.docx` и `reports/report_pr4.pdf`.
Итоговый статус публикации указан в `reports/publication_status.md`.
