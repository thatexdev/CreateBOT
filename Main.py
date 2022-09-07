from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pyfiglet
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep
import os
import time
import requests
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, pyfiglet
from colorama import init, Fore
import os, random
from time import sleep
import speedtest
import inspect

out = pyfiglet.figlet_format("< JVP BOT  >", font="slant")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'អគុណចំពោះការចូលរួម {update.effective_user.first_name}\n\n▪️អ្នកអាចទស្សនារឿងប្រចាំថ្ងៃបាន ហ្វ្រី \n▪️ធ្វើតាមលក្ខខណដើម្បីក្លាយជា PRO USER \n▪️មានរាប់មឿនរឿងសម្រាប់ចែករំលែក \n\nhttps://i.imgur.com/9Qsmsze.jpg  ')
async def channel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'▪ចូលក្នុងឆាណែលយើងខាងក្រោម ដើម្បីបានមើលរឿងសិចប្រចាំថ្ងៃ \nhttps://i.imgur.com/9Qsmsze.jpg  ')
app = ApplicationBuilder().token("5603469076:AAHNCeKtBCtANXcOghMOxIqxLfpyZv8aNkg").build()
print(out)
print(time.strftime(" TIME UTC +7 : %H:%M:%S"))
print('\n                > Your Server Starting .....')

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("channel", channel))

app.run_polling()