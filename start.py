from custom_logging import warning_, error_
from aiogram.utils import executor
from setting.setting_bot import dp
from handler.entry_level import handler_msg
from database import creating_database


# Функция прогрузки файлов
async def on_startup(_):
    try:
        # Базы данных
        creating_database()

        # Хандлеры
        warning_(__file__, 'Бот запущен')
        handler_msg(dp)
    except Exception as e:
        error_(__file__, e)

# Запуск кода
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)