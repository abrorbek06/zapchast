from telebot.types import Message
from example_app.botapp.core.loader import bot
from example_app.botapp.handlers.user.control import start_messages

from example_app.botapp.handlers.user.utils import is_first
from example_app.botapp.keywords.default import language_btn



@bot.message_handler(commands=['start'], chat_types=['private'])
def start_reactions(msg: Message):

    if is_first(msg):
        bot.send_message(
            msg.chat.id,
            text="🌎 Tilni tanlang !",
            reply_markup=language_btn()
        )
    else:
        start_messages(msg)
