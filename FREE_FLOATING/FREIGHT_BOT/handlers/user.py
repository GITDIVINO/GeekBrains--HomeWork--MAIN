from aiogram import types, Dispatcher
from datetime import datetime
import json
from create_bot import dp, write_logs


# greetings
# @dp.message_handler(commands=['start', 'help'])
async def greetings(message: types.Message):
    await message.answer('The FREIGHT_BOT will help you to calculate freight, bunker consumption and intake.\n/help - '
                         'to get instruction\n/vessels_list - to get name of all vessels')
    write_logs(f'\n{datetime.now()} -- USER ID: {message.from_user.id} -- COMMAND "{message.text}" REQUESTED')


# get vessels list
# @dp.message_handler(commands=['vessels_list'])
async def show_vessels_lst(message: types.Message):
    with open(r'vessels\data.json', 'r', encoding='utf-8') as f:
        vessels_lst = 'WAGENBORG SHIPPING:\n'
        data = json.load(f)
        for i in data:
            vessels_lst += f'mv {i.capitalize()}: {data[i]}\n'
        await message.answer(vessels_lst)
        write_logs(f'\n{datetime.now()} -- USER ID: {message.from_user.id} -- "vessels_lst" REQUESTED')


def register_handlers_user(dp : Dispatcher):
    dp.register_message_handler(greetings, commands=['start', 'help'])
    dp.register_message_handler(show_vessels_lst, commands=['vessels_list'])



