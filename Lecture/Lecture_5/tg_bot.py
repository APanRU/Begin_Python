from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token(
    "5980688680:AAEBil6j3zHWB7uwOkMQS3DJuZ6oXaYsw2o").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sum", sum))

app.run_polling()
