from datetime import datetime
from aiogram.utils import executor
from create_bot import write_logs, dp
from handlers import user, exchange, intake


# service info for console/logs
async def on_startup(_):
    write_logs(f'\n\n{datetime.now()} -- |------HELLO, ALDIVINO! FREIGHT BOT IS ONLINE------|')

user.register_handlers_user(dp)
exchange.register_handlers_exchange(dp)
intake.register_handlers_intake(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # polling mode

