from config_data.config import ADMIN_LIST

from States.mystates import MyStates

from funcs.bot_funcs import *

my_state = MyStates()


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


@bot.callback_query_handler(func=lambda call: call.data == "call_premium")
def call_hard(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, CALL_SUBSCRIBE.format(type_sub="Премиум"))


@bot.callback_query_handler(func=lambda call: call.data == "call_medium")
def call_medium(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, CALL_SUBSCRIBE.format(type_sub="Медиум"))


@bot.callback_query_handler(func=lambda call: call.data == "call_lite")
def call_easy(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, CALL_SUBSCRIBE.format(type_sub="Лайт"))


@bot.callback_query_handler(func=lambda call: call.data == "top_up")
def call_top_up_balance(call):
    call_back = call.data
    message = call.message
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton("Нажми на меня", url="https://t.me/yarchkk")
    markup.add(btn_1)
    bot.send_message(chat_id, "Менеджер", reply_markup=markup)
    bot.send_message(chat_id, CALL_TOP_UP)


@bot.message_handler(content_types=['text'], func=lambda msg: check_acces_to_command(msg.from_user.id))
def text_handler(message: Message):
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
