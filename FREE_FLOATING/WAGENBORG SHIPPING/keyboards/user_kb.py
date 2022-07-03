from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json

b1 = KeyboardButton('/WAGENBORG')
b2 = KeyboardButton('/WAGENBORG')

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.dump
    for i in data:
        print(i)

kb_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_vessels = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_user.row(b1)
kb_vessels.row(b2)
