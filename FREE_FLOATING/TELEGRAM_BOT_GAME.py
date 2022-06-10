import telebot

TOKEN = '5316873768:AAF9x8B4B1XB8wm5kzsi_5lAzfMgJhlrImg'
bot = telebot.TeleBot(TOKEN)  # create a bot


@bot.message_handler(commands=["start"])
def start(m, res=False):
    """Function will reply on 'start' bottom"""
    bot.send_message(m.chat.id, 'Привет, как тебя зовут?')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    """Function will reply on text"""
    bot.send_message(message.chat.id, 'Ты сейчас дома?')


# start bot
bot.polling(none_stop=True, interval=0)
