from aiogram import types, Dispatcher
from create_bot import dp


# here bot catch vsl` name and give info
# @dp.message_handler()
async def command_start(message: types.Message):
    if message.text.lower():
        await message.answer()


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
