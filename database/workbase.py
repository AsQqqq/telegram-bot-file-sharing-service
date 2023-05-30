import sqlite3
from setting import database_path
from custom_logging import info_, error_

class client_control():
    def __init__(self):
        try:
            info_(__file__, 'Подключение к базе данных')
            self.connection = sqlite3.Connection(database_path)
            self.cursor = self.connection.cursor()
            self.main_table_name = 'user'
            info_(__file__, 'Успешно подключены')
        except Exception as e:
            error_(__file__, e)
            exit()
    
    def user_exists(self, user_id):
        try:
            info_(__file__, 'Запрос в базу данных user_exists')
            with self.connection:
                result = self.cursor.execute(f"SELECT * FROM {self.main_table_name} WHERE `user_id` = ?",
                    (user_id,)).fetchmany(1)
                return bool(len(result))
        except Exception as e:
            error_(__file__, e)
    
    def user_add(self, user_id, first_name, last_name, full_name, user_name, message_id):
        try:
            info_(__file__, 'Запрос в базу данных user_add')
            with self.connection:
                return self.cursor.execute(f"INSERT INTO {self.main_table_name} \
                    (user_id, first_name, last_name, full_name, user_name, message_id) \
                    VALUES (?, ?, ?, ?, ?, ?)", (user_id, first_name, last_name, full_name, user_name, message_id,))
        except Exception as e:
            error_(__file__, e)
