from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json
from vessels.make_vsl_list import vessels_lst
from keyboards.user_kb import kb_user
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

storage = MemoryStorage()
bot = Bot(token='5485308566:AAEIeTY0SqaR5XKo70zY6QMcEBJixDmG74Q')
dp = Dispatcher(bot, storage=storage)


# greetings
@dp.message_handler(commands=['start', 'help'])
async def command_start(massage: types.Message):
    await bot.send_message(massage.from_user.id, 'The FREIGHT_BOT will help you to calculate voyage, bunker '
                                                 'consumption and intake', reply_markup=kb_user)


class FSMAdmin(StatesGroup):
    PORT_OF_LOADING = State()
    DIST_TO_DISPORT = State()
    VESSEL_NAME = State()
    VESSEL_SPEED = State()
    VESSEL_CONSUMPTION = State()
    VESSEL_CAPACITY = State()
    DATE_OF_BL = State()
    MGO_ROTTERDAM = State()
    RATE_OF_EXCHANGE = State()


# WAGENBORG SHIPPING
@dp.message_handler(commands='WAGENBORG', state=None)
async def command_start(message: types.Message):
    await FSMAdmin.VESSEL_NAME.set()
    await message.reply('What vessel performed the shipment?')


# take info from vessel`s description
@dp.message_handler(commands=vessels_lst, state=FSMAdmin.VESSEL_NAME)
async def command_start(message: types.Message, state: FSMContext):

   ''' async with state.proxy() as data:
        data[vessels_lst] = message.

    with open(r'C:\Users\User\Desktop\GeekBrains\GeekBrains__HomeWork__MAIN\FREE_FLOATING\WAGENBORG '
              r'SHIPPING\vessels\data.json', 'r', encoding='utf-8') as f:
        data = json.load(f) '''

    await FSMAdmin.next()
    await message.reply('Please advise date of BL')
        




        # VESSEL_CONSUMPTION = data[message.text[1:]]['consumption']
        # VESSEL_SPEED = data[message.text[1:]]['speed']
        # VESSEL_CAPACITY = data[message.text[1:]]['consumption']
    # await bot.send_message(message.from_user.id, data[message.text[1:]], reply_markup=ReplyKeyboardRemove())



# def bunker_compensation_calc():
#     eur_bunker_price = MGO_ROTTERDAM / RATE_OF_EXCHANGE - 340
#     return (DIST_TO_DISPORT / 10 / 24) * VESSEL_CONSUMPTION * eur_bunker_price
#
# def voyage_calc():


# @dp.message_handler()
# async def echo_send(massage: types.Message):
#     await massage.answer(massage.text)
#     # await massage.reply(massage.text)


executor.start_polling(dp, skip_updates=True)
