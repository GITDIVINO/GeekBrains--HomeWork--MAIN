from aiogram import types, Dispatcher
from create_bot import dp, write_logs
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from aiogram.dispatcher import FSMContext
from keyboards import kb_user, kb_vessels, kb_months, kb_load_ports, kb_dis_ports
from EUR_USD import scrap_rate_of_exchange
import json


# class for voyage calculator
class VoyageCalculator(StatesGroup):
    VESSEL_NAME = State()
    PORT_OF_LOADING = State()
    PORT_TO_DISCHARGING = State()
    DATE_OF_BL = State()
    SHIPMENT_MONTH = State()
    QUANTITY_AS_PER_BL = State()
    MGO = State()
    distance_to_disport = 992
    freight = 0


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

        if message.text == 'St. Malo':
            VoyageCalculator.distance_to_disport = 992
            VoyageCalculator.freight += 4.25
        elif message.text == 'Le Legue':
            VoyageCalculator.distance_to_disport = 1001
            VoyageCalculator.freight += 4.25
        elif message.text == 'Rotterdam':
            VoyageCalculator.distance_to_disport = 717
        elif message.text == 'Brake':
            VoyageCalculator.distance_to_disport = 505
        elif message.text == 'Bremen':
            VoyageCalculator.distance_to_disport = 525
        elif message.text == 'WC UK':
            VoyageCalculator.distance_to_disport = 1414
        elif message.text == 'EC Ireland':
            VoyageCalculator.distance_to_disport = 1244
        elif message.text == 'Hamburg':
            VoyageCalculator.distance_to_disport = 460
        elif message.text == 'New Holland':
            VoyageCalculator.distance_to_disport = 992
        elif message.text == 'Plymouth':
            VoyageCalculator.distance_to_disport = 992
        elif message.text == 'Teignmouth':
            VoyageCalculator.distance_to_disport = 992
        elif message.text == 'Brest':
            VoyageCalculator.distance_to_disport = 1172
        elif message.text == 'Brugge':
            VoyageCalculator.distance_to_disport = 730

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
        if message.text == 'September':
            VoyageCalculator.freight += 19.5
        if message.text == 'October':
            VoyageCalculator.freight += 20.75
        if message.text == 'November':
            VoyageCalculator.freight += 21.75
        if message.text == 'December':
            VoyageCalculator.freight += 23.10
        if message.text == 'January':
            VoyageCalculator.freight += 23.75
        if message.text == 'February':
            VoyageCalculator.freight += 24.25
        if message.text == 'March':
            VoyageCalculator.freight += 24.25
        if message.text == 'April':
            VoyageCalculator.freight += 22.75
        if message.text == 'May':
            VoyageCalculator.freight += 21.75
        if message.text == 'June':
            VoyageCalculator.freight += 19.5
        if message.text == 'July':
            VoyageCalculator.freight += 19.25
        if message.text == 'August':
            VoyageCalculator.freight += 19.25

    await VoyageCalculator.next()
    await message.answer('What quantity loaded as per cargo manifest?', reply_markup=types.ReplyKeyboardRemove())
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said this"
               f" is {data['SHIPMENT_MONTH'].capitalize()} shipment -->")


# catch cargo quantity and request MGO
# @dp.message_handler(state=VoyageCalculator.QUANTITY_AS_PER_BL)
async def catch_quantity_loaded(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['QUANTITY_AS_PER_BL'] = message.text
    await VoyageCalculator.next()
    await message.answer('Please advise MGO price for Rotterdam')
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) said quantity of cargo loaded"
               f" is {data['QUANTITY_AS_PER_BL'].capitalize()} -->")


# catch MGO and FINISH ---------------------------------------------------------
# @dp.message_handler(state=VoyageCalculator.MGO)
async def catch_mgo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['MGO'] = message.text

        eur_bunker_price = (int(message.text) / float(scrap_rate_of_exchange(data['DATE_OF_BL'])[0])) - 340
        with open(r'vessels\data.json', 'r', encoding='utf-8') as f:
            vsl_data = json.load(f)
            voyage_duration = int(VoyageCalculator.distance_to_disport) / int(vsl_data[data['VESSEL_NAME']]['speed']) / 24
            bunker_compensation = voyage_duration * eur_bunker_price * int(vsl_data[data['VESSEL_NAME']]['consumption'])
            freight_ = int(data['QUANTITY_AS_PER_BL']) * VoyageCalculator.freight
            final_freight = (freight_ + bunker_compensation) / int(data['QUANTITY_AS_PER_BL'])
            result = f"bunker_compensation = {int(VoyageCalculator.distance_to_disport)} \\ " \
                     f"{int(vsl_data[data['VESSEL_NAME']]['speed'])} \\ 24 = {round(voyage_duration, 2)} * " \
                     f"{round(eur_bunker_price, 2)} * {int(vsl_data[data['VESSEL_NAME']]['consumption'])} = " \
                     f"{round(bunker_compensation, 2)}\n" \
                     f"freight = {data['QUANTITY_AS_PER_BL']} mts * {VoyageCalculator.freight} EUR = {freight_} EUR\n" \
                     f"FINAL FREIGHT = ({round(freight_, 2)} + {bunker_compensation}) / {data['QUANTITY_AS_PER_BL']} " \
                     f"mts = {round(final_freight, 2)} EUR"
            print(result)
            VoyageCalculator.freight = 0
    await message.answer(result, reply_markup=kb_user)  # result of calculation
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) insert MGO price"
               f" is {data['MGO']} -->")

    await state.finish()


def register_handlers_voyage_calculator(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['Voyage_calculator'])
    dp.register_message_handler(catch_vsl_name, state=VoyageCalculator.VESSEL_NAME)
    dp.register_message_handler(catch_loading_port, state=VoyageCalculator.PORT_OF_LOADING)
    dp.register_message_handler(catch_discharging_port, state=VoyageCalculator.PORT_TO_DISCHARGING)
    dp.register_message_handler(catch_bl_date, state=VoyageCalculator.DATE_OF_BL)
    dp.register_message_handler(catch_shipment_month, state=VoyageCalculator.SHIPMENT_MONTH)
    dp.register_message_handler(catch_quantity_loaded, state=VoyageCalculator.QUANTITY_AS_PER_BL)
    dp.register_message_handler(catch_mgo, state=VoyageCalculator.MGO)
