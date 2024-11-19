import telebot
import os
from dotenv import load_dotenv
import handler

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    handler.start(bot, message)


@bot.message_handler(content_types=["text"])
def start(message):
    handler.handle_country_text(bot, message)


bot.infinity_polling()
