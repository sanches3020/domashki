import sqlite3
conn = sqlite3.connect('database_name.db')
cursor = conn.cursor() 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS bd (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT,
        name TEXT,
        patronymic TEXT,
        gender TEXT,
        email VARCHAR(255),
        username VARCHAR(255),
        password VARCHAR(255)
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bd1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        file_name TEXT,
        description TEXT
    )
""")

print(cursor.fetchall())
conn.close()
