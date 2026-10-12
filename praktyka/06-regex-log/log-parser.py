
import re
from collections import Counter

# Шаблон для розбору рядків журналу
shablon = re.compile(
    r'^(?P<ip>\d+\.\d+\.\d+\.\d+) - - '
    r'\[(?P<chas>[^\]]+)\] '
    r'"(?P<metod>[A-Z]+) (?P<shlyah>\S+) [^"]*" '
    r'(?P<kod>\d{3})(?:\s|$)'
)

rozibrano = 0
propushcheno = 0

ip_adresy = Counter()
kody = Counter()
pomylky_5xx = []


with open("data/access.log", encoding="utf-8") as f:
    for ryadok in f:
        m = shablon.search(ryadok)

        if not m:
            propushcheno += 1
            continue

        rozibrano += 1

        ip_adresy[m["ip"]] += 1
        kody[m["kod"]] += 1

        
        if m["kod"].startswith("5"):
            pomylky_5xx.append((m["chas"], m["shlyah"]))


# 1. Кількість розібраних і пропущених рядків
print("1. Результати розбору:")
print("Розібрано:", rozibrano)
print("Пропущено:", propushcheno)

# 2. Топ-5 IP-адрес
print("\n2. Топ-5 IP-адрес:")
for adresa, kilkist in ip_adresy.most_common(5):
    print(adresa, "-", kilkist, "запитів")

# 3. Кількість запитів за кодами відповіді
print("\n3. Коди відповіді:")
for kod, kilkist in sorted(kody.items()):
    print(kod, "-", kilkist, "запитів")

print("Різних кодів:", len(kody))

# 4. Запити з помилками 5xx
print("\n4. Запити з помилками 5xx:")
for chas, shlyah in pomylky_5xx:
    print(chas, "-", shlyah)

print("Усього помилок 5xx:", len(pomylky_5xx))
# 2й, 3й та 4й пункт я робила за допомогою ші, тому що моїх знань не вистачало для того щоб зробити ці пункти,але регулярні вирази намагалась писати самостійно,тільки коли була помилка яку я не могла виправити - тоді зверталась до ші.