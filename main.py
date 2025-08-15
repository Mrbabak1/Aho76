import telebot
import os

# توکن رباتت رو اینجا بذار
TOKEN = os.getenv("8197278466:AAEsbz9z0HKlPlCdTvq_nAk5kiYRzCukxnU")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"شما گفتید: {message.text}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
