import sqlite3 as sq

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tourists(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    last_name VARCHAR,
    sex VARCHAR,
    date_of_birth DATE,
    mobile_number VARCHAR,
    email VARCHAR,
    country VARCHAR);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tours(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lable VARCHAR,
    country VARCHAR,
    city VARCHAR,
    start_date DATE,
    end_date DATE,
    price DECIMAL);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS reservations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tourist INT,
    id_tour INT,
    booking_date DATE,
    tourist_count INT,
    FOREIGN KEY (id_tourist) REFERENCES tourists(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_tour) REFERENCES tours(id) ON DELETE CASCADE ON UPDATE CASCADE
    );""")

    if cur.execute("""SELECT * FROM tourists""").fetchall() == []:
        cur.execute("""INSERT INTO tourists (name, last_name, sex, date_of_birth, mobile_number, email, country) VALUES 
    ('Иван', 'Иванов', 'М', '1990-01-01', '+79123456789', 'ivanov@gmail.com', 'Россия'),
    ('Javier', 'Garcia', 'М', '1989-12-30', '+34612345678', 'garcia@gmail.com', 'Spain'),
    ('Hans', 'Müller', 'М', '1993-07-07', '+4915201234567', 'mueller@gmail.com', 'Germany'),
    ('Sophie', 'Schmidt', 'Ж', '1991-11-25', '+4915209876543', 'schmidt@gmail.com', 'Germany'),
    ('Francesco', 'Bianchi', 'М', '1987-06-14', '+393348765432', 'bianchi@gmail.com', 'Italy'),
    ('Giulia', 'Rossi', 'Ж', '1992-09-03', '+393498765432', 'rossi@gmail.com', 'Italy'),
    ('Jane', 'Doe', 'Ж', '1995-03-10', '+14155552672', 'janedoe@gmail.com', 'USA'),
    ('Елена', 'Петрова', 'Ж', '1985-02-15', '+79012345678', 'petrova@mail.ru', 'Россия'),
    ('John', 'Doe', 'М', '1988-05-20', '+14155552671', 'johndoe@gmail.com', 'USA'),
    ('Sofia', 'Martinez', 'Ж', '1994-04-18', '+34698765432', 'martinez@gmail.com', 'Spain');""")
    else:
        pass

    if cur.execute("""SELECT * FROM tours""").fetchall() == []:
        cur.execute("""INSERT INTO tours (lable, country, city, start_date, end_date, price) VALUES 
    ('Испания-путешествие по городам', 'Испания', 'Мадрид', '2021-12-01', '2021-12-12', 10000),
    ('Рио-де-Жанейро-Карнавал', 'Бразилия', 'Рио-де-Жанейро', '2022-02-01', '2022-02-10', 1000),
    ('Конкио-Шопинг', 'Япония', 'Конкио', '2021-09-01', '2021-09-10', 12000),
    ('Нью-Йорк-Городская экскурсия', 'США', 'Нью-Йорк', '2021-08-01', '2021-08-05', 7500),
    ('Греция-Отдых на море', 'Греция', 'Санторини', '2021-11-01', '2020-09-11', 8000),
    ('Бангкок-Тематическая экскурсия по храмам', 'Таиланд', 'Бангкок', '2022-05-01', '2022-05-05', 5000),
    ('Париж-Осмотр достопримечательностей', 'Франция', 'Париж', '2021-10-01', '2021-10-05', 5500),
    ('Лазурный бангок', 'Южная Африка', 'Кейптаун', '2022-04-01', '2022-04-10', 12500),
    ('Барселона-Кулинарный тур', 'Испания', 'Барселона', '2022-03-01', '2022-03-07', 7000),
    ('Полный отдых на море', 'Египет', 'Каир', '2022-06-01', '2022-06-07', 1200);""")
    else:
        pass

    if cur.execute("""SELECT * FROM reservations""").fetchall() == []:
        cur.execute("""INSERT INTO reservations (id_tourist, id_tour, booking_date, tourist_count) VALUES 
    (9, 8, '2022-10-10', 2),
    (3, 1, '2020-12-11', 3),
    (5, 6, '2023-03-22', 2),
    (7, 9, '2022-08-15', 3),
    (1, 3, '2022-09-23', 1),
    (6, 2, '2022-11-18', 4),
    (4, 10, '2022-12-05', 1),
    (2, 5, '2022-07-01', 2),
    (8, 4, '2023-02-14', 2),
    (10, 7, '2023-04-17', 1);""")
    else:
        pass

# SQL-запросы на выборку данных из БД

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    #1 Вывести список всех туристов
    print(cur.execute(f"""SELECT * FROM tourists""").fetchall())
    #2 Вывести список всех туров, отсортированных по цене в порядке убывания
    print(cur.execute(f"""SELECT * FROM tours ORDER BY price DESC""").fetchall())
    #3 Вывести список всех бронирований, сделанных в заданном городе
    print(cur.execute(f"""SELECT * FROM reservations WHERE id_tour in (SELECT id FROM tours WHERE city='Конкио')""").fetchall())
    #4 Вывести список всех туристов, сделавших бронирование в определенный период времени
    print(cur.execute(f"""SELECT * FROM tourists WHERE id in (SELECT id_tourist FROM reservations WHERE booking_date BETWEEN '2022-10-10' AND '2022-11-18')""").fetchall())
    #5 Вывести список всех туров с указанием названия страны и города
    print(cur.execute(f"""SELECT lable,country, city FROM tours""").fetchall())
    #6 Вывести список всех туристов, женщин, у которых дата рождения позже 01.01.1990
    print(cur.execute(f"""SELECT * FROM tourists WHERE sex='Ж' AND date_of_birth>'1990-01-01'""").fetchall())
    #7 Вывести список всех туров, цена которых больше 5000
    print(cur.execute(f"""SELECT * FROM tours WHERE price>5000""").fetchall())
    #8 Вывести список всех туристов, которые сделали бронирование на конкретный тур
    print(cur.execute(f"""SELECT * FROM tourists WHERE id IN (SELECT id_tourist FROM reservations WHERE id_tour IN (SELECT id FROM tours WHERE lable='Лазурный бангок'))""").fetchall())
    #9  Вывести список всех туристов, которые сделали бронирование на тур в указанную дату
    print(cur.execute(f"""SELECT * FROM tourists WHERE id IN (SElECT id_tourist FROM reservations WHERE booking_date='2022-10-10')""").fetchall())
    #10 Вывести список всех туристов, у которых номер телефона начинается на "+7"
    print(cur.execute(f"""SELECT * FROM tourists WHERE mobile_number LIKE '+7%'""").fetchall())

# SQL-запросы на обновление данных в БД:
with sq.connect('tourist.db') as con:
    cur = con.cursor()
    # #1 Изменить дату начала тура с id=1 на '2023-05-01'
    # cur.execute(f"""UPDATE tours SET start_date='2023-05-01' WHERE id=1""")
    # #2 Обновить цену тура с id=7 на 1500
    # cur.execute(f"""UPDATE tours SET price=1500 WHERE id=7""")
    # #3 Изменить номер телефона туриста с id=5 на '+1 (555) 123-4567'
    # cur.execute(f"""UPDATE tourists SET mobile_number='+1 (555) 123-4567' WHERE id=5""")
    # #4 Изменить дату бронирования с id=3 на '2023-04-05'
    # cur.execute(f"""UPDATE reservations SET booking_date='2023-04-05' WHERE id=3""")
    # #5 Обновить количество туристов в бронировании с id=8 на 3
    # cur.execute(f"""UPDATE reservations SET tourist_count=3 WHERE id=8""")
    # #6 Изменить дату окончания тура с id=2 на '2023-08-31'
    # cur.execute(f"""UPDATE tours SET end_date='2023-08-31' WHERE id=2""")
    # #7 Обновить электронную почту туриста с id=1 на 'new_email@example.com'
    # cur.execute(f"""UPDATE tourists SET email='new_email@example.com' WHERE id=1""")
    # #8 Изменить дату начала тура с id=4 на '2023-06-15'
    # cur.execute(f"""UPDATE tours SET start_date='2023-06-15' WHERE id=4""")
    # #9 Обновить дату начала тура на 2023-05-01 для всех туров, где страна = 'Испания'
    # cur.execute(f"""UPDATE tours SET start_date='2023-05-01' WHERE country='Испания'""")
    # #10 Обновление цены на тур "Греция-отдых на море" на 1500 у.е.
    # cur.execute(f"""UPDATE tours SET price=1500 WHERE lable='Греция-отдых на море'""")
    # #11 Обновление даты начала тура "Испания-путешествие по городам" на 2023-06-01
    # cur.execute(f"""UPDATE tours SET start_date='2023-06-01' WHERE lable='Испания-путешествие по городам'""")
    # #12 Обновление количества туристов в бронировании с id 2 на 3 человека
    # cur.execute(f"""UPDATE reservations SET tourist_count=3 WHERE id=2""")
    # #13 Обновление номера телефона у туриста с id 2 на +1 (123) 456-7890
    # cur.execute(f"""UPDATE tourists SET mobile_number='+1 (123) 456-7890' WHERE id=2""")
    # #14 Обновление даты начала тура на 2024-07-01 для всех туров, цена которых меньше 2000 у.е.
    # cur.execute(f"""UPDATE tours SET start_date='2024-07-01' WHERE price<2000""")
    # #15 Обновление электронной почты у всех туристов из России на new_email@example.com
    # cur.execute(f"""UPDATE tourists SET email='new_email@example.com' WHERE country='Россия'""")
    # #16 Обновление даты начала тура на 2023-08-15 для всех бронирований с количеством туристов больше 2
    # cur.execute(f"""UPDATE tours SET start_date='2023-08-15' WHERE id IN (SELECT id_tour FROM reservations WHERE tourist_count>2)""")
    # #17 Обновление названия тура на "Полный отдых на море" для всех бронирований с id_тура равным 3
    # cur.execute(f"""UPDATE tours SET lable='Полный отдых на море' WHERE id=3""")


# SQL-запросы на удаление данных из БД:

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    # #1 Удалить все бронирования, связанные с туристом с id=1
    # cur.execute(f"""DELETE FROM reservations WHERE id_tourist = 1""")
    # #2 Удалить все бронирования, связанные с туром с id=2
    # cur.execute(f"""DELETE FROM reservations WHERE id_tour = 2""")
    # #3 Удалить все бронирования, сделанные в определенную дату
    # cur.execute(f"""DELETE FROM reservations WHERE booking_date='2022-10-10'""")
    # #4  Удалить всех туристов, которые сделали бронирование на тур с id=3
    # cur.execute(f"""DELETE FROM tourists WHERE id IN (SELECT id_tourist FROM reservations WHERE id_tour=3)""")
    # #5 Удалить все бронирования, сделанные туристом с определенным номером телефона
    # cur.execute(f"""DELETE FROM reservations WHERE id_tourist IN (SELECT id FROM tourists WHERE mobile_number='+393498765432')""")
    # #6 Удалить все бронирования, сделанные туристом с определенной электронной почтой
    # cur.execute(f"""DELETE FROM reservations WHERE id_tourist IN (SELECT id FROM tourists WHERE email='mueller@gmail.com')""")
    # #7 Удалить все бронирования на туры, начинающиеся после определенной даты
    # cur.execute(f"""DELETE FROM reservations WHERE booking_date>'2020-12-11'""")
    # #8 Удалить всех туристов, которые забронировали тур в определенную страну
    # cur.execute(f"""DELETE FROM tourists WHERE id IN (SELECT id_tourist FROM reservations WHERE id_tour IN (SELECT id FROM tours WHERE country='Россия'))""")
    # #9 Удалить все бронирования на туры, заканчивающиеся до определенной даты
    # cur.execute(f"""DELETE FROM reservations WHERE id_tour IN (SELECT id FROM tours WHERE end_date < '2022-02-10')""")
    # #10  Удалить все бронирования, сделанные на тур с определенной ценой
    # cur.execute(f"""DELETE FROM reservations WHERE id_tour IN (SELECT id FROM tours WHERE price = '5000')""")
#%%
