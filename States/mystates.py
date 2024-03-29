from telebot.handler_backends import State, StatesGroup


class MyStates(StatesGroup):
    tg_id = State()
    tg_username = State()
    tg_name = State()