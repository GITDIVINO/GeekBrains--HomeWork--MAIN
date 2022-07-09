from aiogram import types, Dispatcher
from create_bot import dp, write_logs
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from aiogram.dispatcher import FSMContext
from keyboards import kb_user, kb_vessels, kb_cargoes
import json


# class for intake calculator
class Intake(StatesGroup):
    NAME_OF_VESSEL = State()
    CARGO_NAME = State()


# start Intake store
# @dp.message_handler(commands=['/Intake_calculator'])
async def intake_start(message: types.Message):
    await Intake.NAME_OF_VESSEL.set()
    await message.answer('Please enter name of the vessel?', reply_markup=kb_vessels)
    write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is requesting to count intake -->')


# catch vessel`s name and request cargo name
# @dp.message_handler(state=Intake.NAME_OF_VESSEL)
async def catch_name_vsl(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['NAME_OF_VESSEL'] = message.text
    await Intake.next()
    await message.answer('Please advise name of the cargo?', reply_markup=kb_cargoes)
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said the vessel`s "
               f"name is {data['NAME_OF_VESSEL'].capitalize()} -->")


# catch cargo name and FINISH ---------------------------------------------------------
# @dp.message_handler(state=Intake.CARGO_NAME)
async def catch_cargo_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['CARGO_NAME'] = message.text   # this is not necessary, but i`ll leave it here
        with open(r'vessels\data.json', 'r', encoding='utf-8') as f:
            result = 'WAGENBORG SHIPPING:\n'
            vsl_data = json.load(f)
            async with state.proxy() as data:
                if message.text == 'RSM':
                    intake_ = f"Vessel`s intake is {vsl_data[data['NAME_OF_VESSEL']]['capacity']//58} mts"
                elif message.text == 'SBM':
                    intake_ = f"Vessel`s intake is {vsl_data[data['NAME_OF_VESSEL']]['capacity']//57} mts"
                elif message.text == 'SH':
                    intake_ = f"Vessel`s intake is {vsl_data[data['NAME_OF_VESSEL']]['capacity']//54} mts"
        await message.answer(intake_, reply_markup=kb_user)  # result of calculation
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) received '{intake_}' -->")
    await state.finish()


def register_handlers_intake(dp : Dispatcher):
    dp.register_message_handler(intake_start, commands=['Intake_calculator'])
    dp.register_message_handler(catch_name_vsl, state=Intake.NAME_OF_VESSEL)
    dp.register_message_handler(catch_cargo_name, state=Intake.CARGO_NAME)


