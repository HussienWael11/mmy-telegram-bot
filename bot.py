from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8837950383:AAGa7iErhTtGdQnt8Cz3kz_wUkPVCvz_VbA"

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "ا":
        await update.message.reply_text("البوت شغال ✅")

  app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

print("Bot is running...")
app.run_polling()
