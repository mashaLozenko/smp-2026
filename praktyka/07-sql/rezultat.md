# Результати практичної роботи 7

## 1. Вивід перевірки SQL-запитів

```text
== 1. Треки, довші за 5 хвилин: назва, тривалість у секундах; від найдовшого
     Name | Seconds
     Occupation / Precipice | 5286.953
     Through a Looking Glass | 5088.838
     Greetings from Earth, Pt. 1 | 2960.293
     … ще 1066
  ✅ правильно (рядків: 1069)

== 2. Виконавці на A, за абеткою
     Name
     A Cor Do Som
     AC/DC
     Aaron Copland & London Symphony Orchestra
     … ще 23
  ✅ правильно (рядків: 26)

== 3. Сім найдорожчих рахунків: номер, дата, країна, сума; від найбільшої
     InvoiceId | InvoiceDate | BillingCountry | Total
     404 | 2025-11-13 00:00:00 | Czech Republic | 25.86
     299 | 2024-08-05 00:00:00 | USA | 23.86
     96 | 2022-02-18 00:00:00 | Hungary | 21.86
     … ще 4
  ✅ правильно (рядків: 7)

== 4. Клієнти з Польщі або Чехії: імʼя, прізвище, країна
     FirstName | LastName | Country
     František | Wichterlová | Czech Republic
     Helena | Holý | Czech Republic
     Stanisław | Wójcik | Poland
  ✅ правильно (рядків: 3)

== 5. Приватні клієнти з Канади (Company порожнє): імʼя, прізвище, місто
     FirstName | LastName | City
     François | Tremblay | Montréal
     Robert | Brown | Toronto
     Edward | Francis | Ottawa
     … ще 3
  ✅ правильно (рядків: 6)

== 6. Країни клієнтів без повторів, за абеткою
     Country
     Argentina
     Australia
     Austria
     … ще 21
  ✅ правильно (рядків: 24)

== 7. Альбоми зі словом Live у назві
     Title
     Alcohol Fueled Brewtality Live! [Disc 1]
     Alcohol Fueled Brewtality Live! [Disc 2]
     Acústico MTV [Live]
     … ще 14
  ✅ правильно (рядків: 17)

== 8. Рахунки за березень 2025: номер, дата, країна, сума; за датою
     InvoiceId | InvoiceDate | BillingCountry | Total
     345 | 2025-03-01 00:00:00 | Germany | 3.96
     346 | 2025-03-02 00:00:00 | France | 5.94
     347 | 2025-03-05 00:00:00 | Italy | 8.91
     … ще 4
  ✅ правильно (рядків: 7)

Разом: 8 з 8 пунктів ✅   (мінімум для зарахування — пункти 1–5)
```

## 2. Результат роботи циклу Python

```text
Усього клієнтів: 59
Helena Holý Czech Republic
František Wichterlová Czech Republic
Stanisław Wójcik Poland
```

## 3. Порівняння циклу Python і SQL-запиту

У SQL мені вистачило одного запиту, щоб знайти клієнтів із Польщі та Чехії, а в Python для цього довелося написати цикл, умову, `append()` і сортування. Якщо клієнтів буде не 59, а 5 мільйонів, Python доведеться спочатку отримати всі записи й перебрати їх, тому це може зайняти більше часу та пам'яті. У циклі я сама перевіряю країну кожного клієнта, додаю потрібних до списку та сортую їх за прізвищем. А в SQL я просто задаю умови, і база даних сама знаходить потрібних клієнтів, а за потреби може також їх відсортувати.