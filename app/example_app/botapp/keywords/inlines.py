from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from example_app.models import ConfirmChannel

from .default import buttons


def subscription_inline_btn(channels, lang):
    markup = InlineKeyboardMarkup(row_width=1)
    not_channel = [username for username in channels.keys() if channels[str(username)] == False]
    for channel in not_channel:
        name = ConfirmChannel.objects.get(username=channel).name
        markup.add(InlineKeyboardButton(text=name, url=f"https://t.me/{channel.replace('@', '')}/"))

    confirm = InlineKeyboardButton(text=buttons['confirm'][lang], callback_data='confirm')
    markup.add(confirm)
    return markup


