from telebot import types
import countries as countries_data

countries = countries_data.countries


def markup_continent(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = []

    for continent in countries.keys():
        btn = types.KeyboardButton(continent)
        btns.append(btn)
    markup.add(*btns)

    bot.send_message(message.chat.id, "Choose a continent", reply_markup=markup)
