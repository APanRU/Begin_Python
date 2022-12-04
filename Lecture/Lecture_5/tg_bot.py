from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token(
    "you_token").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sum", sum))

app.run_polling()
