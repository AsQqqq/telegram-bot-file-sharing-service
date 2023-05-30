from aiogram import types
from setting.setting_bot import bot, dp
from database import clientbase
from custom_logging import info_, error_

# Основная функция
@dp.message_handler(commands='start')
async def start(message: types.Message):
    try:
        info_(__file__, 'Написал пользователь команду /start')
        user_id = message.from_user.id
        if not clientbase.user_exists(user_id=user_id):
            clientbase.user_add(user_id=user_id, first_name=message.from_user.first_name, last_name=message.from_user.last_name, 
                full_name=message.from_user.full_name, user_name=message.from_user.username, message_id=0)
            await bot.send_message(chat_id=user_id, text='Пользователь добавлен')
        else:
            await bot.send_message(chat_id=user_id, text='Привет')
    except Exception as e:
        error_(__file__, e)

# Ловля сообщений которые неизвестны боту
async def other(message: types.Message):
    try:
        info_(__file__, 'Поймана неизвестная команда')
        user_id = message.from_user.id
        await bot.send_message(chat_id=user_id, text=message.text)
    except Exception as e:
        error_(__file__, e)


# Регистрация функций
def handler_msg(dp):
    dp.register_message_handler(other)
