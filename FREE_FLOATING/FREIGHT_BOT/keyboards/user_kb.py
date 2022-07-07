from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Voyage calculator')
b2 = KeyboardButton('Vessel`s description')
b3 = KeyboardButton('EUR-USD rate of exchange')
b4 = KeyboardButton('Intake calculator')

kb_user = ReplyKeyboardMarkup()
kb_user.add(b1).add(b2).add(b3).add(b4)







