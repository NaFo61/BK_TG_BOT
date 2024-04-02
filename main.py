from config_data.config import ADMIN_LIST
from loader import bot

from telebot import types
from telebot.types import Message

from States.mystates import MyStates

from texts.texts import *

my_state = MyStates()

blocked_users: dict = {}
blocked_users.setdefault(6554422345, {'acces_to_command': False})
print(blocked_users)


def check_acces_to_command(user_id) -> bool:
    if check_in_users(user_id) is True:
        if blocked_users[user_id]['acces_to_command'] is False:
            return False
    return True


def check_in_users(user_id) -> bool:
    if user_id in blocked_users:
        return True
    return False


@bot.message_handler(commands=['start'], func=lambda msg: check_acces_to_command(msg.from_user.id))
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
    btn_4 = types.KeyboardButton(START_MARKUP_BTN_4)
    markup.add(btn_1, btn_2)
    markup.add(btn_3, btn_4)

    bot.send_sticker(chat_id, sticker=START_STICKER)
    mes = MESSAGE_START.format(name_user=telegram_name)
    bot.send_message(chat_id, mes, reply_markup=markup)


@bot.message_handler(commands=['help'], func=lambda msg: check_acces_to_command(msg.from_user.id))
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
    bot.send_sticker(chat_id, HELP_STICKER)
    bot.send_message(chat_id, MESSAGE_HELP, reply_markup=markup)


@bot.message_handler(commands=["admin"])
def admin_handler(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id in ADMIN_LIST:
        bot.send_message(chat_id, ADMIN_SUCCESS)
        markup = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(ADMIN_MARKUP_BTN_1, callback_data="rasulka")
        btn_2 = types.InlineKeyboardButton(ADMIN_MARKUP_BTN_2, callback_data="ban")
        btn_3 = types.InlineKeyboardButton(ADMIN_MARKUP_BTN_3, callback_data="unban")
        btn_4 = types.InlineKeyboardButton(ADMIN_MARKUP_BTN_4, callback_data="balance")
        btn_5 = types.InlineKeyboardButton(ADMIN_MARKUP_BTN_5, callback_data="give_test_period")
        btn_6 = types.InlineKeyboardButton(ADMIN_MARKUP_BTN_6, callback_data="get_stat")
        markup.add(btn_1)
        markup.add(btn_2, btn_3)
        markup.add(btn_4, btn_5)
        markup.add(btn_6)
        bot.send_message(chat_id, ADMIN_CHOOSE_FUNC, reply_markup=markup)
    else:
        bot.send_message(chat_id, ADMIN_DENIED)


@bot.callback_query_handler(func=lambda call: call.data == "rasulka")
def call_rasulka(call):
    call_back = call.data
    print(call)
    print(call_back)
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, ADMIN_MARKUP_BTN_1)


@bot.callback_query_handler(func=lambda call: call.data == "ban")
def call_ban(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, ADMIN_MARKUP_BTN_2)
    bot.register_next_step_handler(msg, ban)


def ban(message: Message):
    chat_id = message.chat.id
    who = message.text
    print(blocked_users)
    if int(who) in blocked_users.keys():
        bot.send_message(chat_id, ALREADY_IN_BAN.format(who=who))
    else:
        blocked_users.setdefault(int(who), {'acces_to_command': False})
        bot.send_message(chat_id, USER_ADDED_IN_BAN.format(who=who))


@bot.callback_query_handler(func=lambda call: call.data == "unban")
def call_unban(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, ADMIN_MARKUP_BTN_3)


@bot.callback_query_handler(func=lambda call: call.data == "balance")
def call_rasulka(call):
    call_back = call.data
    print(call)
    print(call_back)
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, ADMIN_MARKUP_BTN_4)


@bot.callback_query_handler(func=lambda call: call.data == "give_test_period")
def call_rasulka(call):
    call_back = call.data
    print(call)
    print(call_back)
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, ADMIN_MARKUP_BTN_5)


@bot.callback_query_handler(func=lambda call: call.data == "get_stat")
def call_rasulka(call):
    call_back = call.data
    print(call)
    print(call_back)
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, ADMIN_MARKUP_BTN_6)


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
    btn_1 = types.InlineKeyboardButton("call_hard", callback_data="call_hard")
    btn_2 = types.InlineKeyboardButton("call_medium", callback_data="call_medium")
    btn_3 = types.InlineKeyboardButton("call_easy", callback_data="call_easy")
    markup.add(btn_1)
    markup.add(btn_2)
    markup.add(btn_3)
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(chat_id, photo=photo)
    bot.send_message(chat_id, "Наши ценники", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "call_hard")
def call_hard(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, "Вы выбрали call_hard")


@bot.callback_query_handler(func=lambda call: call.data == "call_medium")
def call_medium(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, "Вы выбрали call_medium")


@bot.callback_query_handler(func=lambda call: call.data == "call_easy")
def call_easy(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, "Вы выбрали call_easy")


def show_profile(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton("Пополнить", callback_data="popolnit")
    markup.add(btn_1)
    bot.send_message(chat_id, "БАЛАНС\nУслуга\nДата", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "popolnit")
def popolnit(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, "Вы выбрали popolnit")


@bot.message_handler(content_types=['text'], func=lambda msg: check_acces_to_command(msg.from_user.id))
def run(message: Message):
    chat_id = message.chat.id
    user_message = message.text

    if user_message == START_MARKUP_BTN_1:
        print(START_MARKUP_BTN_1)
        bot.send_sticker(chat_id, START__BTN_1_STICKER)
        bot.send_message(chat_id, TEST_PERIOD_MESSAGE)
    elif user_message == START_MARKUP_BTN_2:
        print("START_MARKUP_BTN_2")
        help_handler(message)
    elif user_message == START_MARKUP_BTN_3:
        print("START_MARKUP_BTN_3")
        show_profile(message)
    elif user_message == START_MARKUP_BTN_4:
        print("START_MARKUP_BTN_4")
        prices(message)
    elif user_message == HELP_MARKUP_BTN_1:
        print("HELP_MARKUP_BTN_1")
        show_admin(message)
    elif user_message == HELP_MARKUP_BTN_2:
        print("HELP_MARKUP_BTN_2")
        show_faq(message)
    elif user_message == HELP_MARKUP_BTN_3:
        print("HELP_MARKUP_BTN_3")
        suggest(message)
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
