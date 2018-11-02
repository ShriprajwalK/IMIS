import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


def read_from_db():
    c.execute('SELECT * FROM db.sqlite3')
    data = c.fetchall()
    print(data)


read_from_db()
