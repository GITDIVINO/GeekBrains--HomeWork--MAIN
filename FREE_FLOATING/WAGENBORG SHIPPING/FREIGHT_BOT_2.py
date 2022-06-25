from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json
from vessels.make_vsl_list import vessels_lst
from keyboards.user_kb import kb_user
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5485308566:AAEIeTY0SqaR5XKo70zY6QMcEBJixDmG74Q')
dp = Dispatcher(bot, storage=storage)


# greetings
@dp.message_handler(commands=['start', 'help'])
async def command_start(massage: types.Message):
    await bot.send_message(massage.from_user.id, 'The FREIGTH_BOT will help you to calculate voyage, bunker '
                                                 'consumption and intake with Wagenborg Shipping. Please choose name '
                                                 'of the vessel', reply_markup=kb_user)


PORT_OF_LOADING = ''
DIST_TO_DISPORT = ''
VESSEL_NAME = ''
VESSEL_SPEED = ''
VESSEL_CONSUMPTION = ''
VESSEL_CAPACITY = ''
DATE_OF_BL = ''
MGO_ROTTERDAM = ''
RATE_OF_EXCHANGE = ''


# take info from vessel`s description
@dp.message_handler(commands=vessels_lst)
async def command_start(message: types.Message):
    with open(r'C:\Users\User\Desktop\GeekBrains\GeekBrains__HomeWork__MAIN\FREE_FLOATING\WAGENBORG '
              r'SHIPPING\vessels\data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        VESSEL_NAME = message.text[1:]
        VESSEL_CONSUMPTION = data[message.text[1:]]['consumption']
        VESSEL_SPEED = data[message.text[1:]]['speed']
        VESSEL_CAPACITY = data[message.text[1:]]['consumption']
    await bot.send_message(message.from_user.id, data[message.text[1:]], reply_markup=ReplyKeyboardRemove())


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
