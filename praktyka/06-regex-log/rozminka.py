# 1.1. Читання файлу та виведення великими літерами

with open("data/words.txt", encoding="utf-8") as f:
    for ryadok in f:
        print(ryadok.rstrip().upper())

# 1.2. Пошук значень X-DSPAM-Confidence та обчислення середнього

suma = 0
kilkist = 0

with open("data/mbox-short.txt", encoding="utf-8") as f:
    for ryadok in f:
        if ryadok.startswith("X-DSPAM-Confidence:"):
            chislo = float(ryadok.split(":")[1])
            suma += chislo
            kilkist += 1

serednie = suma / kilkist

print("Кількість рядків:", kilkist)
print("Середнє значення:", serednie)

