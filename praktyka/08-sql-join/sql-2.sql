-- Робота 8. SQL: обʼєднання і агрегація. База data/chinook.db
-- Під кожним рядком «-- N.» — ОДИН запит. Рядки з «--» — коментарі, їх можна дописувати.
-- Перевірка:  python praktyka/08-sql-join/perevir.py

-- 1. Треки гурту Queen: трек, альбом
SELECT Track.Name AS Track, Album.Title AS Album
FROM Track
JOIN Album ON Track.AlbumId = Album.AlbumId
JOIN Artist ON Album.ArtistId = Artist.ArtistId
WHERE Artist.Name = 'Queen';

-- 2. Скільки треків у кожному жанрі: жанр, кількість; від найбільшого
SELECT Genre.Name AS Genre, COUNT(*) AS TrackCount
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.GenreId, Genre.Name
ORDER BY TrackCount DESC;

-- 3. Топ-10 клієнтів за сумою покупок: імʼя, прізвище, сума; від найбільшої
SELECT Customer.FirstName, Customer.LastName,
       SUM(Invoice.Total) AS TotalSpent
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY TotalSpent DESC
LIMIT 10;

-- 4. Виконавці, у яких більше 5 альбомів: виконавець, альбомів; від найбільшого
SELECT Artist.Name AS Artist, COUNT(Album.AlbumId) AS AlbumCount
FROM Artist
JOIN Album ON Artist.ArtistId = Album.ArtistId
GROUP BY Artist.ArtistId, Artist.Name
HAVING COUNT(Album.AlbumId) > 5
ORDER BY AlbumCount DESC;

-- 5. Виконавці без жодного альбому
SELECT Artist.Name
FROM Artist
LEFT JOIN Album ON Artist.ArtistId = Album.ArtistId
WHERE Album.AlbumId IS NULL;

-- 6. Середня тривалість треку по жанрах, у хвилинах з одним знаком: жанр, хвилин; від найдовшої
SELECT Genre.Name AS Genre,
       ROUND(AVG(Track.Milliseconds) / 60000.0, 1) AS Minutes
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.GenreId, Genre.Name
ORDER BY Minutes DESC;

-- 7. Виторг за країнами (за рахунками): країна, сума; від найбільшого
SELECT BillingCountry AS Country, SUM(Total) AS Revenue
FROM Invoice
GROUP BY BillingCountry
ORDER BY Revenue DESC;

-- 8. Співробітники підтримки й скільки клієнтів у кожного: імʼя, прізвище, клієнтів; від найбільшого
SELECT Employee.FirstName, Employee.LastName,
       COUNT(Customer.CustomerId) AS CustomerCount
FROM Employee
JOIN Customer ON Employee.EmployeeId = Customer.SupportRepId
GROUP BY Employee.EmployeeId, Employee.FirstName, Employee.LastName
ORDER BY CustomerCount DESC;
