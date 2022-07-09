from aiogram import types, Dispatcher
from create_bot import dp
from EUR_USD import scrap_rate_of_exchange
from create_bot import dp, write_logs
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from aiogram.dispatcher import FSMContext
from keyboards import kb_user


# class for Rate of Exchange
class RateExchange(StatesGroup):
    DATE_BL = State()


# start RateExchange store
# @dp.message_handler(commands=['EUR_USD_exchange'])
async def request_bl_date(message: types.Message):
    await RateExchange.DATE_BL.set()
    await message.answer('Please enter date of B/L:')
    write_logs(f'\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) is requesting "EUR-USD rate" -->')


# catch DATE_OF_BL and FINISH ---------------------------------------------------------
# @dp.message_handler(state=RateExchange.DATE_BL)
async def show_usd_eur_exchange(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['DATE_BL'] = message.text
        rate_ = f"[{scrap_rate_of_exchange(message.text)[1]}] USD - EUR: {scrap_rate_of_exchange(message.text)[0]}"
        await message.answer(rate_, reply_markup=kb_user)  # result of calculation
    write_logs(f"\n{datetime.now()} -- Human (USER ID: {message.from_user.id}) received {rate_} -->")
    await state.finish()


def register_handlers_exchange(dp : Dispatcher):
    dp.register_message_handler(request_bl_date, commands=['EUR_USD_exchange'])
    dp.register_message_handler(show_usd_eur_exchange, state=RateExchange.DATE_BL)
