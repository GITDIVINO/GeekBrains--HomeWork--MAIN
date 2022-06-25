from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/adamas')
b2 = KeyboardButton('/ankie')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_user.row(b1, b2)




