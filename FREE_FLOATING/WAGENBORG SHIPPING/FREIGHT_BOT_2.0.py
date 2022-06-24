from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json
from vessels.make_vsl_list import vessels_lst

bot = Bot(token='5485308566:AAEIeTY0SqaR5XKo70zY6QMcEBJixDmG74Q')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start(massage: types.Message):
    await bot.send_message(massage.from_user.id, 'The FREIGTH_BOT can help you to calculate voyage, bunker consumption '
                                                 'and intake with Wagenborg Shipping. Please enter name of the vessel')


@dp.message_handler(commands=vessels_lst)
async def command_start(message: types.Message):
    with open(r'C:\Users\User\Desktop\GeekBrains\GeekBrains__HomeWork__MAIN\FREE_FLOATING\WAGENBORG '
              r'SHIPPING\vessels\data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    await bot.send_message(message.from_user.id, data[message.text[1:]])


# @dp.message_handler()
# async def echo_send(massage: types.Message):
#     await massage.answer(massage.text)
#     # await massage.reply(massage.text)


executor.start_polling(dp, skip_updates=True)
