from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from FREIGHT_BOT_2 import dp


class FSMAdmin(StatesGroup):
    VESSEL_NAME = State()
    VESSEL_CONSUMPTION = State()
    VESSEL_SPEED = State()
    VESSEL_CAPACITY = State()


# Beginning of the dialog
@dp.massage_handler(commands='Upload', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Upload photo')
