from aiogram import types, Dispatcher
from datetime import datetime
import json
from create_bot import dp, write_logs
from keyboards import kb_user, kb_vessels, kb_load_ports, kb_dis_ports, kb_months, kb_cargoes
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


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


# class for voyage calculator
class VoyageCalculator(StatesGroup):
    VESSEL_NAME = State()
    PORT_OF_LOADING = State()
    PORT_TO_DISCHARGING = State()
    DATE_OF_BL = State()
    SHIPMENT_MONTH = State()
    QUANTITY_AS_PER_BL = State()


# start VoyageCalculator store
# @dp.message_handler(commands='/Voyage_calculator', state=None)
async def command_start(message: types.Message):
    await VoyageCalculator.VESSEL_NAME.set()
    await message.answer('What vessel performed the shipment?', reply_markup=kb_vessels)
    write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is asking to calculate voyage -->')


# catch vessel`s name and request loading port
# @dp.message_handler(state=VoyageCalculator.VESSEL_NAME)
async def catch_vsl_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['VESSEL_NAME'] = message.text
    await VoyageCalculator.next()
    await message.answer('Please advise Port of Loading?', reply_markup=kb_load_ports)
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said the vessel`s "
               f"name is {data['VESSEL_NAME'].capitalize()} -->")


# catch loading port and request discharging port
# @dp.message_handler(state=VoyageCalculator.PORT_OF_LOADING)
async def catch_loading_port(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['PORT_OF_LOADING'] = message.text
    await VoyageCalculator.next()
    await message.answer('Please advise Port of discharging?', reply_markup=kb_dis_ports)
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said Port of Loading"
               f" is {data['PORT_OF_LOADING'].capitalize()} -->")


# catch discharging port and request date of B/L
# @dp.message_handler(state=VoyageCalculator.PORT_TO_DISCHARGING)
async def catch_discharging_port(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['PORT_TO_DISCHARGING'] = message.text
    await VoyageCalculator.next()
    await message.answer('Please advise date of B/L in format "yyyy-mm-dd"', reply_markup=types.ReplyKeyboardRemove())
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said Port of Discharging"
               f" is {data['PORT_TO_DISCHARGING'].capitalize()} -->")


# catch date of B/L and request shipment`s month
# @dp.message_handler(state=VoyageCalculator.DATE_OF_BL)
async def catch_bl_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['DATE_OF_BL'] = message.text
    await VoyageCalculator.next()
    await message.answer('What month of this shipment?', reply_markup=kb_months)
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said cargo was loaded"
               f" on {data['DATE_OF_BL'].capitalize()} -->")


# catch shipment`s month and request cargo quantity loaded
# @dp.message_handler(state=VoyageCalculator.SHIPMENT_MONTH)
async def catch_shipment_month(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['SHIPMENT_MONTH'] = message.text
    await VoyageCalculator.next()
    await message.answer('What quantity loaded as per cargo manifest?', reply_markup=types.ReplyKeyboardRemove())
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said this"
               f" is {data['SHIPMENT_MONTH'].capitalize()} shipment -->")


# catch cargo quantity loaded and FINISH ---------------------------------------------------------
# @dp.message_handler(state=VoyageCalculator.QUANTITY_AS_PER_BL)
async def catch_quantity_loaded(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['QUANTITY_AS_PER_BL'] = message.text
    await message.answer('FINISH')  # result of calculation
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said quantity of cargo loaded"
               f" is {data['QUANTITY_AS_PER_BL'].capitalize()} -->")

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(greetings, commands=['start', 'help'])

    dp.register_message_handler(show_vessels_lst, commands=['vessels_list'])

    dp.register_message_handler(command_start, commands=['Voyage_calculator'])
    dp.register_message_handler(catch_vsl_name, state=VoyageCalculator.VESSEL_NAME)
    dp.register_message_handler(catch_loading_port, state=VoyageCalculator.PORT_OF_LOADING)
    dp.register_message_handler(catch_discharging_port, state=VoyageCalculator.PORT_TO_DISCHARGING)
    dp.register_message_handler(catch_bl_date, state=VoyageCalculator.DATE_OF_BL)
    dp.register_message_handler(catch_shipment_month, state=VoyageCalculator.SHIPMENT_MONTH)
    dp.register_message_handler(catch_quantity_loaded, state=VoyageCalculator.QUANTITY_AS_PER_BL)




