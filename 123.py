# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect("films_db.sqlite")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
cur.execute("INSERT INTO test VALUES(2, '{1}','{2}')")
result = cur.execute("""SELECT * FROM test""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem)
con.commit()
con.close()

