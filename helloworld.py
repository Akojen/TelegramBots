import json
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging


def get_api_key(file):
    #Reads api info from json file
    with open(file, 'r') as f:
        return json.load(f)


apidict = get_api_key('telegramApi.json')

# Following https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot

updater = Updater(token=apidict['token'], use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello World ... ( ͡° ͜ʖ ͡°)")


def main ():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

if __name__ == "__main__":
    main()