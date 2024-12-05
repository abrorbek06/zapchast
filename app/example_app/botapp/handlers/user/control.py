
from django.conf import settings
import os


from example_app.botapp.core.state import UserState
from telebot.types import Message, ReplyKeyboardRemove
from example_app.botapp.core.loader import bot
from example_app.botapp.keywords.default import *
from example_app.botapp.keywords.inlines import  *
from example_app.models import *
from example_app.botapp.core.src.language import get_lang

from .utils import product_media, is_first

language = lambda chat_id: TelUser.objects.get(tg_id=chat_id).language


message = get_lang()["messages"]


def start_messages(msg: Message):
    chat_id = msg.from_user.id
    user = TelUser.objects.get(tg_id=chat_id)
    user_language = user.language

    result = check_subscription(chat_id)

    if not all(result.values()):
        joiner_subscription(msg)
        return

    img_path = os.path.join(settings.STATICFILES_DIRS[0], 'buttons_img', 'start.png')

    if not Customer.objects.filter(tg_user=user).exists():
        reply_markup = register_btn(user_language)
    else:
        reply_markup = start_btn(user_language, chat_id)

    with open(img_path, 'rb') as f:
        img = f.read()

        welcome_message = message['welcome_message'].get(user_language, "Welcome!")
        bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=welcome_message,
            reply_markup=reply_markup
        )


def check_subscription(chat_id):
    data = {}
    try:
        # Kanal ro'yxatini olish
        channels = ConfirmChannel.objects.all()  # Django modelini ishlatish

        for channel in channels:
            # Foydalanuvchining kanalga a'zoligini tekshirish
            member = bot.get_chat_member(channel.username, chat_id)

            # A'zolik holatini tekshirish
            if member.status in ['member', 'administrator', 'creator']:
                data[str(channel.username)] = True
            else:
                data[str(channel.username)] = False

        return data
    except Exception as e:
        # bot.send_message(chat_id, f"Xatolik yuz berdi: {e}")
        return {}

def joiner_subscription(msg: Message):
    chat_id = msg.from_user.id
    channels = check_subscription(chat_id)
    bot.send_message(chat_id, text=message['join_channels'][language(chat_id)], reply_markup=subscription_inline_btn(channels, language(chat_id)))

def communication(msg: Message):
    chat_id = msg.from_user.id
    bot.send_message(chat_id, text=message['communication_info'][language(chat_id)])

def account(msg: Message):
    chat_id = msg.from_user.id
    user_info = Customer.objects.get(tg_user__tg_id=chat_id)
    text = message['user_info'][language(chat_id)].format(name=user_info.name, contact=user_info.contact)
    bot.send_message(chat_id, text=text)

def spare_parts(msg: Message):
    chat_id = msg.from_user.id
    bot.send_message(chat_id=chat_id, text=msg.text, reply_markup=spare_parts_btn(language(chat_id)))

def send_products(msg: Message):
    chat_id = msg.from_user.id
    bot.send_message(chat_id=chat_id, text=msg.text, reply_markup=send_products_btn(language(chat_id), msg.text))

def send_product_items(msg: Message):
    chat_id = msg.from_user.id
    product = Product.objects.get(name=msg.text)
    # with open(product.image.path, 'rb') as f:
    bot.send_message(chat_id=chat_id, text=msg.text, reply_markup=back_btn(language(chat_id)))
    bot.send_media_group(chat_id=chat_id, media=product_media(product))

def send_settings(msg: Message):
    chat_id = msg.from_user.id
    bot.send_message(chat_id=chat_id, text=message['settings_section'][language(chat_id)], reply_markup=settings_btn(language(chat_id), chat_id))

def change_language(msg: Message):
    chat_id = msg.from_user.id
    bot.send_message(chat_id, text=message['select_language'][language(chat_id)], reply_markup=language_btn())

def register_new_customer(user):
    chat_id = user.tg_id
    user_id = user.tg_id
    bot.set_state(user_id, UserState.name, chat_id)
    bot.send_message(chat_id, text=message["enter_name"][user.language], reply_markup=ReplyKeyboardRemove())

@bot.message_handler(content_types=['text'], state=UserState.name)
def reaction_lastname(msg: Message):
    chat_id = msg.chat.id
    user_id = msg.from_user.id

    language = TelUser.objects.get(tg_id=user_id).language

    with bot.retrieve_data(user_id, chat_id) as data:
        data['name'] = msg.text.capitalize()
    bot.set_state(user_id, UserState.contact, chat_id)
    bot.send_message(chat_id,
                     text=message["enter_phone"][language],
                     reply_markup=contact_btn(language), parse_mode='html')

@bot.message_handler(content_types=['contact', 'text'], state=UserState.contact)
def reaction_contact(msg: Message):
    chat_id = msg.chat.id
    user_id = msg.from_user.id
    user = TelUser.objects.get(tg_id=user_id)
    language = user.language
    with bot.retrieve_data(user_id, chat_id) as data:
        if msg.content_type == 'contact':
            data['contact'] = msg.contact.phone_number
            # bot.set_state(user_id, UserState.submit, chat_id)
            # text = message["verify_info"][language].format(data['name'], data['contact'])

        else:
            import re
            if re.match(r'^\+998(9(0|1|3|4|5|7|8|9)|33|77|88|55)\d{7}$', msg.text):
                data['contact'] = msg.text
                # bot.set_state(user_id, UserState.submit, chat_id)
                # text = message["verify_info"][language].format(data['name'], data['contact'])

            else:
                bot.set_state(user_id, UserState.contact, chat_id)
                bot.send_message(chat_id,
                                 text=message["incorrect_phone"][language],
                                 reply_markup=contact_btn(language))
                return

        updated, created = Customer.objects.update_or_create(
            tg_user=user,
            defaults={'name': data['name'], 'contact': data['contact'], }
        )
        print(2)
        if created:
            bot.send_message(msg.chat.id, message["data_saved"][language],
                             reply_markup=start_btn(language, user.tg_id))
            bot.delete_state(user_id)
            print(3)
            return


    bot.send_message(msg.chat.id, message["data_updated"][language], reply_markup=start_btn(language, user.tg_id))
    bot.delete_state(user_id)

