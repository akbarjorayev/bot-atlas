import markup


def start(bot, message):
    bot.send_message(message.chat.id, "Hi it's Akbar's Atlas bot")
    markup.markup_continent(bot, message)
