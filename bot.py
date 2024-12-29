import telebot
import os
from flask import Flask, request
from dotenv import load_dotenv
import handler
from webhook.setup import set_webhook

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    handler.start(bot, message)


@bot.message_handler(content_types=["text"])
def start(message):
    handler.handle_country_text(bot, message)


flask_app = Flask(__name__)


@flask_app.route("/webhook", methods=["POST"])
def webhook():
    json_data = request.get_json()
    if json_data:
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
    return "ok", 200


if __name__ == "__main__":
    set_webhook()
    flask_app.run(host="0.0.0.0", port=8000)
