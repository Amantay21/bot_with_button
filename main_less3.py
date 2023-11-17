import telebot
from telebot import types

bot = telebot.TeleBot("6608715523:AAF9rMJd4RPqsLgFxaVTiu9-O0L9sfGLhHE", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Info')
    btn2 = types.KeyboardButton('Data')
    btn3 = types.KeyboardButton('Help')
    markup.row(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)

@bot.message_handler(commands=['info'])
def info(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('Отправить фото', callback_data='send'))
    bot.send_message(message.chat.id, 'Info', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    file = open('./some.jpeg', 'rb')
    bot.send_photo(message.chat.id, file)


bot.polling(none_stop=True)