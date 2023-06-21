import sqlite3

connect = sqlite3.connect('Библиотека.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Авторы(
    КодАвтора INTEGER PRIMARY KEY,
    Фамилия VARCHAR,
    Имя VARCHAR,
    FOREIGN KEY(КодАвтора) references АвторКниги(КодАвтора)
    )
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS Книги(
    КодКниги INTEGER PRIMARY KEY,
    Название VARCHAR,
    Раздел VARCHAR,
    Издательство VARCHAR,
    ГодИздания INTEGER,
    МестоХранения VARCHAR
    )
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS Разделы(
    Раздел VARCHAR,
    FOREIGN KEY(Раздел) references Книги(Раздел)
    )
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS Издательства(
    Издательство VARCHAR,
    Город VARCHAR,
    FOREIGN KEY(Издательство) references Книги(Издательство)
    )
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS АвторКниги(
    КодАвтораКниги INTEGER PRIMARY KEY,
    КодКниги INTEGER,
    КодАвтора INTEGER,
    FOREIGN KEY(КодКниги) references Книги(КодКниги)
    )
    """)
