from aiogram import types, Dispatcher
from datetime import datetime
import json
from create_bot import dp, write_logs
from keyboards import kb_user, kb_vessels, kb_load_ports
from aiogram.dispatcher.filters.state import State, StatesGroup
from vessels.make_vsl_list import vessels_lst
from aiogram.dispatcher import FSMContext


# greetings
# @dp.message_handler(commands=['start', 'help'])
async def greetings(message: types.Message):
    await message.answer('The FREIGHT_BOT will help you to calculate freight, bunker consumption and intake.\n/help - '
                         'to get instruction\n/vessels_list - to get name of all vessels', reply_markup=kb_user)
    write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is needed for my HELP -->')


# get vessels list
# @dp.message_handler(commands=['vessels_list'])
async def show_vessels_lst(message: types.Message):
    with open(r'vessels\data.json', 'r', encoding='utf-8') as f:
        result = 'WAGENBORG SHIPPING:\n'
        data = json.load(f)
        for i in data:
            result += f'mv {i.capitalize()} : {data[i]}\n'
        await message.answer(result)
        write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is requesting "vessels_lst" -->')


class VoyageCalculator(StatesGroup):
    VESSEL_NAME = State()
    PORT_OF_LOADING = State()
    DIST_TO_DISPORT = State()
    DATE_OF_BL = State()


@dp.message_handler(commands='/Voyage_calculator', state=None)
async def command_start(message: types.Message):
    await VoyageCalculator.VESSEL_NAME.set()
    await message.answer('What vessel performed the shipment?', reply_markup=kb_vessels)
    write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is asking to calculate voyage -->')


@dp.message_handler(state=VoyageCalculator.VESSEL_NAME)
async def load_vsl_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['VESSEL_NAME'] = message.text
    await VoyageCalculator.next()
    await message.answer('Please advise Port of loading?', reply_markup=kb_load_ports)
    write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said the vessel` '
               f'name is {message.text.capitalize()} -->')


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(greetings, commands=['start', 'help'])
    dp.register_message_handler(show_vessels_lst, commands=['vessels_list'])
    dp.register_message_handler(command_start, commands=['Voyage_calculator'])
