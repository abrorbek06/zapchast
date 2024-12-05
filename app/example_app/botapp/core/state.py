
from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    name = State()
    contact = State()
    submit = State()


class SenderState(StatesGroup):
    name = State()
