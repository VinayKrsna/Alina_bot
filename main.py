import telebot


bot = telebot.TeleBot('1745883082:AAEv78t_tEk6clmnXj26cR9B6OZU79Igty0')

@bot.message_handler()
def start_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Получить PDF-книгу “Со100яние”', callback_data='get_book'))
    url_button = telebot.types.InlineKeyboardButton(text="Подписаться на Instagram Алины",
                                                    url="https://www.instagram.com/alannadey/")
    keyboard.add(url_button)
    # keyboard.row(telebot.types.InlineKeyboardButton('Подписаться на Instagram Алины', callback_data='get_inst'))
    bot.send_message(
        message.chat.id,
        f' Привет, {message.from_user.username}! \n' +
        'Тебя приветствует Бот Со100яния. \n' +
        'Я могу тебе помочь: ',
        reply_markup=keyboard)
    bot.send_message(
        message.chat.id,
        'С чего начнешь?)')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "get_book":
        bot.send_document(call.message.chat.id, open(r'C:/Uni/Bot/so100ianie_book.pdf', 'rb'))


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
