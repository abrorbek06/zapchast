import os

from django.conf import settings
from telebot.types import CallbackQuery

from example_app.botapp.core.loader import bot

from example_app.botapp.handlers.user.control import *

from example_app.models import Customer, TelUser



@bot.callback_query_handler(func=lambda call: "confirm" in call.data)
def control_handler(call: CallbackQuery):
    print(call.data)
    chat_id = call.from_user.id
    result = check_subscription(chat_id)
    user = TelUser.objects.get(tg_id=chat_id)
    if not all(result.values()):
        channels = check_subscription(chat_id)
        bot.send_message(chat_id, text=message['join_channels'][language(chat_id)],
                         reply_markup=subscription_inline_btn(channels, language(chat_id)))

        return
    else:
        img_path = os.path.join(settings.STATICFILES_DIRS[0], 'buttons_img', 'start.png')

        if not Customer.objects.filter(tg_user=user).exists():
            reply_markup = register_btn(language(chat_id))
        else:
            reply_markup = start_btn(language(chat_id), chat_id)

        with open(img_path, 'rb') as f:
            img = f.read()

            welcome_message = message['welcome_message'].get(language(chat_id), "Welcome!")
            bot.send_photo(
                chat_id=chat_id,
                photo=img,
                caption=welcome_message,
                reply_markup=reply_markup
            )
