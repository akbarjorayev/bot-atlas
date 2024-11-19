import markup
import countries as countries_data
import sender

countries = countries_data.countries


def handle_country_text(bot, message):
    if message.text == "Back to continents":
        markup.markup_continent(bot, message)
        return

    if message.text in countries.keys():
        markup.markup_country(bot, message, message.text)
    else:
        sender.send_country_data(bot, message)
