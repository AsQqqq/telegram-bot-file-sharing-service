from aiogram.dispatcher.filters.state import StatesGroup, State

# Создание машины состояний
class MainState(StatesGroup):
    menu = State()
    upload_file = State()
    entering_token = State()
    managing_downloads = State()