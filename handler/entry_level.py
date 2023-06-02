from aiogram import types
from setting.setting_bot import bot, dp
from database import clientbase
from state import MainState
from keyboard import main_kbd
from aiogram.dispatcher import FSMContext
from custom_logging import info_, error_, warning_

"""MAIN"""

def update_user_info(message, user_id):
    clientbase.update_old_info(user_id=user_id, first_name=message.from_user.first_name, last_name=message.from_user.last_name, 
                full_name=message.from_user.full_name, user_name=message.from_user.username)

# Основная функция
@dp.message_handler(commands='start', state="*")
async def start(message: types.Message, state: FSMContext):
    try:
        info_(__file__, 'Написал пользователь команду /start')
        user_id = message.from_user.id
        try:
            await message.delete()
        except:
            pass
        if not clientbase.user_exists(user_id=user_id):
            clientbase.user_add(user_id=user_id, first_name=message.from_user.first_name, last_name=message.from_user.last_name, 
                full_name=message.from_user.full_name, user_name=message.from_user.username, message_id=0)
            msg = await bot.send_message(chat_id=user_id, text='Пользователь добавлен')
        else:
            update_user_info(message=message, user_id=user_id)
            msg = await bot.send_message(chat_id=user_id, text='Привет', reply_markup=main_kbd().main_menu())
        try:
            await bot.delete_message(chat_id=user_id, message_id=clientbase.select_message_id(user_id=user_id))
        except:
            pass
        clientbase.update_message_id(message_id=msg.message_id, user_id=user_id)
        await MainState.menu.set()
    except Exception as e:
        error_(__file__, e)

# Ловля сообщений которые неизвестны боту
async def other(message: types.Message, state: FSMContext):
    try:
        info_(__file__, 'Поймана неизвестная команда')
        user_id = message.from_user.id
        await bot.send_message(chat_id=user_id, text=message.text)
    except Exception as e:
        error_(__file__, e)

@dp.callback_query_handler(text='back', state="*")
async def back(call: types.CallbackQuery, state: FSMContext):
    try:
        info_(__file__, 'Вы вернулись назад')
        get_state = await state.get_state()
        user_id = call.from_user.id
        if get_state == "MainState:upload_file":
            await bot.edit_message_text(text='Привет', chat_id=user_id, message_id=clientbase.select_message_id(user_id=user_id),
            reply_markup=main_kbd().main_menu())
            await MainState.menu.set()
    except Exception as e:
        error_(__file__, e)

"""KEYBOARD"""

# Нажата кнопка upload_file
@dp.callback_query_handler(text='upload_file', state='MainState:menu')
async def upload_file_kbd(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.answer()
        info_(__file__, 'Нажата кнопка upload_file')
        user_id = call.from_user.id
        warning_(__file__, clientbase.select_message_id(user_id=user_id))
        await bot.edit_message_text(text='Нажата кнопка upload_file', chat_id=user_id, message_id=clientbase.select_message_id(user_id=user_id),
            reply_markup=main_kbd().upload_file())
        await MainState.upload_file.set()
    except Exception as e:
        error_(__file__, e)

# Нажата кнопка entering_token
@dp.callback_query_handler(text='entering_token', state='MainState:menu')
async def entering_token_kbd(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.answer()
        info_(__file__, 'Нажата кнопка entering_token')
        user_id = call.from_user.id
        await bot.send_message(chat_id=user_id, text='Нажата кнопка entering_token')
        await MainState.entering_token.set()
    except Exception as e:
        error_(__file__, e)

# Нажата кнопка managing_downloads
@dp.callback_query_handler(text='managing_downloads', state='MainState:menu')
async def managing_downloads_kbd(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.answer()
        info_(__file__, 'Нажата кнопка managing_downloads')
        user_id = call.from_user.id
        await bot.send_message(chat_id=user_id, text='Нажата кнопка managing_downloads')
        await MainState.managing_downloads.set()
    except Exception as e:
        error_(__file__, e)

# Регистрация функций
def handler_msg(dp):
    dp.register_message_handler(other, state="*")
