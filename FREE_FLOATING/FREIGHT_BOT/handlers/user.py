from aiogram import types, Dispatcher
from datetime import datetime
import json
from create_bot import dp, write_logs
from keyboards import kb_user


# greetings
# @dp.message_handler(commands=['start', 'help'])
async def greetings(message: types.Message):
    await message.answer('The FREIGHT_BOT will help you to calculate freight, bunker consumption and intake.\n\n'
                         '/help - to get this instruction\n'
                         '/vessels_list - to get name of all vessels\n'
                         '/Voyage_calculator - to calculate voyage\n'
                         '/EUR_USD_exchange - to get EUR_USD rate\n'
                         '/Intake_calculator - to calculate holds intake\n', reply_markup=kb_user)
    write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is needed for my HELP -->')


# get vessels list
# @dp.message_handler(commands=['vessels_list'])
async def show_vessels_lst(message: types.Message):
    with open(r'vessels\data.json', 'r', encoding='utf-8') as f:
        result = 'WAGENBORG SHIPPING:\n'
        data = json.load(f)
        for i in data:
            result += f'mv {i.title()} : {data[i]["consumption"]} mts, ' \
                      f'{data[i]["speed"]} kn, {data[i]["capacity"]} cbft\n'
        await message.answer(result, reply_markup=kb_user)
        write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is requesting "vessels_lst" -->')


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(greetings, commands=['start', 'help'])
    dp.register_message_handler(show_vessels_lst, commands=['vessels_list'])

