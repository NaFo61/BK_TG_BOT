from loader import bot

from telebot import types
from telebot.types import Message

from States.mystates import MyStates

from texts.texts import *

my_state = MyStates()


@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    chat_id = message.chat.id
    telegram_id = message.from_user.id
    telegram_name = message.from_user.first_name

    my_state.tg_id = telegram_id
    my_state.tg_username = telegram_name

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton(START_MARKUP_BTN_1)
    btn_2 = types.KeyboardButton(START_MARKUP_BTN_2)
    btn_3 = types.KeyboardButton(START_MARKUP_BTN_3)
    markup.add(btn_1)
    markup.add(btn_2)
    markup.add(btn_3)

    mes = MESSAGE_START.format(name_user=telegram_name)
    bot.send_message(chat_id, mes, reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_handler(message: Message):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton(HELP_MARKUP_BTN_1)
    btn_2 = types.KeyboardButton(HELP_MARKUP_BTN_2)
    btn_3 = types.KeyboardButton(HELP_MARKUP_BTN_3)
    btn_4 = types.KeyboardButton(HELP_MARKUP_BTN_4)
    markup.add(btn_1)
    markup.add(btn_2)
    markup.add(btn_3)
    markup.add(btn_4)
    bot.send_message(chat_id, MESSAGE_HELP, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def run(message: Message):
    chat_id = message.chat.id
    user_message = message.text

    if user_message == START_MARKUP_BTN_1:
        print("START_MARKUP_BTN_1")
    elif user_message == START_MARKUP_BTN_2:
        print("START_MARKUP_BTN_2")
        help_handler(message)
    elif user_message == START_MARKUP_BTN_3:
        print("START_MARKUP_BTN_3")
    elif user_message == HELP_MARKUP_BTN_1:
        print("HELP_MARKUP_BTN_1")
    elif user_message == HELP_MARKUP_BTN_2:
        print("HELP_MARKUP_BTN_2")
    elif user_message == HELP_MARKUP_BTN_3:
        print("HELP_MARKUP_BTN_3")
    elif user_message == HELP_MARKUP_BTN_4:
        print("HELP_MARKUP_BTN_4")
        start_handler(message)
    elif user_message == UNEXPECTED_TEXT_MARKUP_BTN_1:
        print("UNEXPECTED_TEXT_MARKUP_BTN_1")
        start_handler(message)
    elif user_message == UNEXPECTED_TEXT_MARKUP_BTN_2:
        print("UNEXPECTED_TEXT_MARKUP_BTN_2")
        help_handler(message)
    elif user_message == UNEXPECTED_TEXT_MARKUP_BTN_3:
        print("UNEXPECTED_TEXT_MARKUP_BTN_3")
        start_handler(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton(UNEXPECTED_TEXT_MARKUP_BTN_1)
        btn_2 = types.KeyboardButton(UNEXPECTED_TEXT_MARKUP_BTN_2)
        markup.add(btn_1)
        markup.add(btn_2)
        bot.send_message(chat_id, MESSAGE_UNEXPECTED_TEXT, reply_markup=markup)


if __name__ == '__main__':
    print(START_MESSAGE)
    bot.polling(none_stop=True)
