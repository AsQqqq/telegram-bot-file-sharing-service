from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class main_kbd:
    def __init__(self):
        self.back = InlineKeyboardButton(text='Вернуться', callback_data='back')

    def main_menu(self):
        upload_file = InlineKeyboardButton(text='Загрузить файл', callback_data='upload_file')
        entering_token = InlineKeyboardButton(text='Ввести токен', callback_data='entering_token')
        managing_downloads = InlineKeyboardButton(text='Управление загрузками', callback_data='managing_downloads')

        return InlineKeyboardMarkup().add(upload_file).add(entering_token).insert(managing_downloads)
    
    def upload_file(self):
        return InlineKeyboardMarkup().add(self.back)