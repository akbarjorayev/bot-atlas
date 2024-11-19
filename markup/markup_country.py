from telebot import types
import countries as countries_data

countries = countries_data.countries


def markup_country(bot, message, continent):
    if continent in countries:
        btns = []
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn = types.KeyboardButton("Back to continents")
        markup.add(btn)

        for country in countries[continent]:
            country_btn = types.KeyboardButton(country)
            btns.append(country_btn)
        markup.add(*btns)

        bot.send_message(message.chat.id, "Choose a county", reply_markup=markup)
    else:
        bot.send_message(
            message.chat.id,
            f"<b><i>{message.text}</i></b> is not continent",
            parse_mode="html",
        )
