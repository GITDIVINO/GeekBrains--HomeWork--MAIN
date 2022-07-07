from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)


# func writing logs in file 'BOT_LOGS.txt'
def write_logs(any_data):
    with open('BOT_LOGS.txt', 'a', encoding='utf-8') as f:
        f.write(any_data)
        print(any_data)




