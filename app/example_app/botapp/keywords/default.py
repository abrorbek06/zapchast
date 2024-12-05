from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from example_app.models import *
from example_app.botapp.core.src.language import get_lang


buttons = get_lang()['buttons']


def language_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in [v for v in get_lang()['languages'].values()]:
        markup.add(i)
    return markup


def start_btn(lang, chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    spare_parts = KeyboardButton(buttons['spare_parts'][lang])
    settings = KeyboardButton(buttons['settings'][lang])
    communication = KeyboardButton(buttons['communication'][lang])
    markup.add(spare_parts)
    markup.add(communication, settings)
    return markup


def settings_btn(lang, chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    change_language = KeyboardButton(buttons['change_language'][lang])
    account = KeyboardButton(buttons['account'][lang])
    back = KeyboardButton(buttons['back'][lang])

    markup.add(change_language, account, back)
    return markup


def contact_btn(lang):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = KeyboardButton(text=buttons["share_contact"][lang], request_contact=True)
    markup.add(button)
    return markup

def submit_btn(lang):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    submit = KeyboardButton(text=buttons["correct"][lang])
    mistake = KeyboardButton(text=buttons["incorrect"][lang])

    markup.add(submit, mistake)
    return markup

def register_btn(lang):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    register = KeyboardButton(text=buttons["registration"][lang])
    markup.add(register)
    return markup


def spare_parts_btn(lang):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    models = Model.objects.all().values_list('name', flat=True)
    buttons_app = []
    for model in models:
        buttons_app.append(KeyboardButton(model))
    markup.add(*buttons_app)
    back = KeyboardButton(buttons['back'][lang])
    markup.add(back)
    return markup

def send_products_btn(lang, name):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    try:
        model = Model.objects.get(name=name)
        products = Product.objects.filter(model=model)
        buttons_app = []
        for product in products:
            buttons_app.append(KeyboardButton(product.name))
        markup.add(*buttons_app)
    except Model.DoesNotExist:
        pass

    back = KeyboardButton(buttons['back'][lang])
    markup.add(back)
    return markup


def back_btn(lang):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    back = KeyboardButton(buttons['back_product'][lang])
    markup.add(back)
    return markup
