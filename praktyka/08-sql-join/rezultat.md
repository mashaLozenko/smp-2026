# Результати практичної роботи 8

## 1. Результат перевірки

```text
== 1. Треки гурту Queen: трек, альбом
     Track | Album
     A Kind Of Magic | Greatest Hits II
     Under Pressure | Greatest Hits II
     Radio GA GA | Greatest Hits II
     … ще 42
  ✅ правильно (рядків: 45)

== 2. Треків у кожному жанрі: жанр, кількість; від найбільшого
     Genre | TrackCount
     Rock | 1297
     Latin | 579
     Metal | 374
     … ще 22
  ✅ правильно (рядків: 25)

== 3. Топ-10 клієнтів за сумою покупок: імʼя, прізвище, сума; від найбільшої
     FirstName | LastName | TotalSpent
     Helena | Holý | 49.620000000000005
     Richard | Cunningham | 47.620000000000005
     Luis | Rojas | 46.62
     … ще 7
  ✅ правильно (рядків: 10)

== 4. Виконавці з більш ніж 5 альбомами: виконавець, альбомів; від найбільшого
     Artist | AlbumCount
     Iron Maiden | 21
     Led Zeppelin | 14
     Deep Purple | 11
     … ще 3
  ✅ правильно (рядків: 6)

== 5. Виконавці без жодного альбому
     Name
     Milton Nascimento & Bebeto
     Azymuth
     João Gilberto
     … ще 68
  ✅ правильно (рядків: 71)

== 6. Середня тривалість треку по жанрах, хв з одним знаком; від найдовшої
     Genre | Minutes
     Sci Fi & Fantasy | 48.5
     Science Fiction | 43.8
     Drama | 42.9
     … ще 22
  ✅ правильно (рядків: 25)

== 7. Виторг за країнами (за рахунками): країна, сума; від найбільшого
     Country | Revenue
     USA | 523.0600000000003
     Canada | 303.9599999999999
     France | 195.09999999999994
     … ще 21
  ✅ правильно (рядків: 24)

== 8. Співробітники підтримки й кількість їхніх клієнтів; від найбільшого
     FirstName | LastName | CustomerCount
     Jane | Peacock | 21
     Margaret | Park | 20
     Steve | Johnson | 18
  ✅ правильно (рядків: 3)

Разом: 8 з 8 пунктів ✅   (мінімум для зарахування — пункти 1–5)
```

## 2. Моє питання до бази даних

Який жанр музики найчастіше купують клієнти нашого магазину?

## 3. Мій SQL-запит

```sql
SELECT Genre.Name AS Genre,
       SUM(InvoiceLine.Quantity) AS Purchases
FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.GenreId, Genre.Name
ORDER BY Purchases DESC;
```

### Перші рядки результату

```text
Genre               | Purchases
Rock                | 835
Latin               | 386
Metal               | 264
Alternative & Punk  | 244
Jazz                | 80
Blues               | 61
TV Shows            | 47
R&B/Soul            | 41
Classical           | 41
Reggae              | 30
```

## 4. Відповідь

Найчастіше клієнти нашого магазину купують музику жанру Rock — усього було продано 835 треків цього жанру.