# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
# from keyboards import kb_user
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from create_bot import dp
#
# # in case of wrong data entered use 'cancel'
# # @dp.message_handler(state="*", commands='cancel')
# # @dp.message_handler(Text(equals='cancel', ignore_case=True, state="*")
# async def cancel_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#    await state.finish()
#    await message.an('OK', reply_markup=kb_user)
#
#
# def register_handlers_cancel(dp : Dispatcher):
#     dp.register_message_handler(cancel_handler, state="*", commands='cancel')
#     dp.register_message_handler(Text(equals='cancel', ignore_case=True, state="*")

