from custom_logging import clear_, info_
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from setting.config import API

# Отчистка терминала
clear_()

# Создание доступа к оперативной памяти
storage = MemoryStorage()

# Настройки бота
bot = Bot(API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
info_(__file__, 'Настройки созданы')
