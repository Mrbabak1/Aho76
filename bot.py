import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# فعال‌سازی لاگینگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# توکن ربات تلگرام خود را اینجا قرار دهید
TOKEN = '8197278466:AAEsbz9z0HKlPlCdTvq_nAk5kiYRzCukxnU'

# تابع برای فرمان /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! من ربات تلگرام شما هستم.')

# تابع اصلی برای راه‌اندازی ربات
def main() -> None:
    updater = Updater(TOKEN)

    # ثبت فرمان /start
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
