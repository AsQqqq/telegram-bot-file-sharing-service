from setting import database_path
from custom_logging import error_, info_
import sqlite3 as sq

# Создание базы данных
def creating_database():
    try:
        info_(__file__, 'Попытка создание базы данных')
        base = sq.connect(database_path)
        base.execute(""
        "CREATE TABLE IF NOT EXISTS user("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "user_id INTEGER NOT NULL,"
        "first_name TEXT NOT NULL,"
        "last_name TEXT NOT NULL,"
        "full_name TEXT NOT NULL,"
        "user_name TEXT NOT NULL,"
        "message_id INTEGER NOT NULL"
        ")")
    except Exception as e:
        error_(__file__, e)