from example_app.botapp.core.loader import bot
from example_app.botapp.handlers.user.control import *
from example_app.botapp.handlers.user.utils import *
from telebot.types import Message

from example_app.botapp.core.src.language import get_lang
from example_app.models import *


languages = get_lang()
buttons = get_lang()["buttons"]

@bot.message_handler(content_types=['text'], chat_types=['private'])
def main_data(msg: Message):
    print(msg.text)
    bot.send_chat_action(chat_id=msg.chat.id, action="typing")
    chat_id = msg.from_user.id
    user_text = msg.text
    user = TelUser.objects.get(tg_id=chat_id)
    user_lang = user.language

    result = check_subscription(chat_id)

    if buttons['registration'][user_lang] == user_text:
        register_new_customer(user)
        return

    if not all(result.values()):
        joiner_subscription(msg)
        return

    action_map = {

        # MAIN todo main page
        buttons['spare_parts'][user_lang]: spare_parts,
        buttons['settings'][user_lang]: send_settings,
        buttons['back'][user_lang]: start_messages,
        buttons['change_language'][user_lang]: change_language,
        buttons['communication'][user_lang]: communication,
        buttons['account'][user_lang]: account,
        buttons['back_product'][user_lang]: spare_parts

    }


    if user_text in action_map:
        action_map[user_text](msg)
        return

    if user_text in languages['languages'].values():
        update_language_start(msg)
        start_messages(msg)
        return

    if user_text in Model.objects.all().values_list('name', flat=True):
        send_products(msg)
        return

    if user_text in Product.objects.all().values_list('name', flat=True):
        send_product_items(msg)
        return







