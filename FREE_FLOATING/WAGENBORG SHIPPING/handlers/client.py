from aiogram import types
from FINAL_BOT/vessels/make_vsl_list import vessels_lst


# greetings
@dp.message_handler(commands=['start', 'help'])
async def command_start(massage: types.Message):
    await bot.send_message(massage.from_user.id, 'The FREIGTH_BOT can help you to calculate voyage, bunker consumption '
                                                 'and intake with Wagenborg Shipping. Please enter name of the vessel', reply_markup=kb_client)

# take info from folder with vessels
@dp.message_handler(commands=vessels_lst)
async def command_start(message: types.Message):
    with open(r'C:\Users\User\Desktop\GeekBrains\GeekBrains__HomeWork__MAIN\FREE_FLOATING\WAGENBORG '
              r'SHIPPING\vessels\data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    await bot.send_message(message.from_user.id, data[message.text[1:]])
