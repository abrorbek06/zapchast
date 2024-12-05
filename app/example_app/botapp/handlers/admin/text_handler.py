import time
from example_app.botapp.core.loader import bot
from telebot.types import Message
from example_app.botapp.core.state import SenderState
from example_app.models import TelUser
from telebot.types import InputMediaPhoto


@bot.message_handler(commands=['send_ads'])
def start(msg: Message):
    chat_id = msg.chat.id

    # Admin tekshiruvi
    if chat_id in TelUser.objects.filter(is_admin=True).values_list('tg_id', flat=True):
        user_id = msg.from_user.id
        bot.set_state(user_id, SenderState.name, chat_id)
        bot.send_message(chat_id, text="Yubormoqchi bo'lgan xabaringizni yuboring !")


@bot.message_handler(state=SenderState.name, content_types=['text', 'voice', 'video', 'audio', 'photo', 'document'])
def send_ads(msg: Message):
    chat_id = msg.chat.id
    user_id = msg.from_user.id
    users = TelUser.objects.all().values_list('tg_id', flat=True)
    count = 1
    for user in users:
        try:
            # Foydalanuvchidan xabarni nusxalash va yuborish
            bot.copy_message(chat_id=user, from_chat_id=chat_id, message_id=msg.message_id)
            time.sleep(0.1)  # Tezlikni cheklash
            count += 1
        except Exception as e:
            print(f"Xatolik: {e}")
            pass

    bot.delete_state(user_id)
    bot.send_message(chat_id, text=f"{len(users)}tada {count} taga yuborildi !")