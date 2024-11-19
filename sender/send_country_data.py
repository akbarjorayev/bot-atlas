import imgs
import urls
import countries as countries_data


def send_country_data(bot, message):
    country_name = message.text
    try:
        country_imgs = imgs.img_load_flag_emblem(country_name)

        for key, value in country_imgs.items():
            if value:
                caption = f"{key.capitalize()} of {country_name}"
                bot.send_photo(message.chat.id, urls.url_modify(value), caption)

        bot.send_message(
            message.chat.id,
            countries_data.get_country_data(country_name),
            parse_mode="html",
        )
    except:
        bot.send_message(
            message.chat.id,
            f"There is not any data about <b><i>{country_name}</i></b>",
            parse_mode="html",
        )
