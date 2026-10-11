# Передбачення: що Python прочитає з pastky.yaml

| Ключ | Моє передбачення: значення і тип | Показав perevir.py |
|---|---|---|
| svitlo | False, тип boolean | False — логічне значення (bool) |
| pochatok | "2026-09-28", тип string, бо це дата, записана текстом | datetime.date(2026, 9, 28) — дата (date) |
| kod_dostupu | 10, тип integer | 8 — ціле число (int) |
| limit | 1000, тип integer | '1e3' — рядок (str) |
| port | "0x1F90", тип string, бо тут є і букви, і цифри | 8080 — ціле число (int) |
| komentar | "~", тип string | None — порожнє значення (NoneType) |