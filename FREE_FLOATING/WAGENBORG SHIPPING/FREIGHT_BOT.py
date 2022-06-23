import telebot

# Create object
bot = telebot.TeleBot('5485308566:AAEIeTY0SqaR5XKo70zY6QMcEBJixDmG74Q')


# /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Let`s calculate voyage with Wagenborg Shipping\nPlease enter name of the vessel')


# Handle message
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'djlkglk')


# Start bot
bot.polling(none_stop=True, interval=0)
