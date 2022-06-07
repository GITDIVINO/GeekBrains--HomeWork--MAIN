import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('5331721270:AAF-H1RRDkMzskjy_ShO0h-DeWvTSm-vwMQ')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, чем я могу помочь?')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Извини, я ничего не помнимаю')
# Запускаем бота
bot.polling(none_stop=True, interval=0)