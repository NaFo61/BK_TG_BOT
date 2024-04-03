from loader import bot

from telebot import types
from telebot.types import Message
from texts.texts import *

blocked_users: dict = {}
blocked_users.setdefault(6554422345, {'acces_to_command': False})


def check_acces_to_command(user_id) -> bool:
    if check_in_users(user_id) is True:
        if blocked_users[user_id]['acces_to_command'] is False:
            return False
    return True


def check_in_users(user_id) -> bool:
    if user_id in blocked_users:
        return True
    return False


def ban(message: Message):
    chat_id = message.chat.id
    who = message.text
    print(blocked_users)
    if int(who) in blocked_users.keys():
        bot.send_message(chat_id, ALREADY_IN_BAN.format(who=who))
    else:
        blocked_users.setdefault(int(who), {'acces_to_command': False})
        bot.send_message(chat_id, USER_ADDED_IN_BAN.format(who=who))


def show_admin(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton("Админ", url="https://t.me/yarchkk")
    btn_2 = types.InlineKeyboardButton("Модер", url="https://t.me/yaros_sm")
    markup.add(btn_1, btn_2)
    bot.send_message(chat_id, "Наши модеры", reply_markup=markup)


def show_faq(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Вопрос / ответ")


def suggest(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Предложить")


def prices(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(PRICES_BTN_1, callback_data="call_premium")
    btn_2 = types.InlineKeyboardButton(PRICES_BTN_2, callback_data="call_medium")
    btn_3 = types.InlineKeyboardButton(PRICES_BTN_3, callback_data="call_lite")
    markup.add(btn_1)
    markup.add(btn_2)
    markup.add(btn_3)
    with open("/Users/yaroslav/Downloads/prices.jpg", "rb") as photo:
        bot.send_photo(chat_id, photo=photo)
    bot.send_message(chat_id, PRICES_MESSAGE, reply_markup=markup)


def show_profile(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(SHOW_PROFILE_BTN, callback_data="top_up")
    markup.add(btn_1)
    bot.send_message(chat_id, SHOW_PROFILE_MESSAGE, reply_markup=markup)