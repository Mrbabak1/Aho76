import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")  # از متغیر محیطی می‌خونه

def edit_caption(update, context):
    if update.message.caption:
        new_caption = update.message.caption.replace("قدیمی", "جدید")
        if update.message.document:
            context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=update.message.document.file_id,
                caption=new_caption
            )
        elif update.message.photo:
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=update.message.photo[-1].file_id,
                caption=new_caption
            )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.document | Filters.photo, edit_caption))

updater.start_polling()
