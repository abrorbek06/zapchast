
from telebot.types import Message, InputMediaPhoto
from example_app.models import *
from example_app.botapp.core.src.language import get_lang


languages = get_lang()
message = get_lang()["messages"]


def update_language_start(msg: Message):
    language = msg.text
    lange = languages['languages']
    user = TelUser.objects.get(tg_id=msg.from_user.id)
    user.language = [v for v in lange.keys() if lange.get(v) == language][0]
    user.save()


def is_first(msg: Message):
    tg_id = msg.from_user.id
    username = msg.from_user.username
    fullname = msg.from_user.full_name
    user, created = TelUser.objects.get_or_create(
        tg_id=tg_id,
        defaults={
            'username': username,
            'fullname': fullname,
        }
    )

    if created:
        print(f"New user created: {user}")
        return True
    else:
        updated = False
        if user.username != username:
            user.username = username
            updated = True
        if user.fullname != fullname:
            user.fullname = fullname
            updated = True

        if updated:
            user.save()
            print(f"User updated: {user}")

        return False




def product_media(product):
    media = []
    first_caption = True  # Faqat birinchi rasmga izoh qo'shish uchun

    if product.product_media.exists():  # Agar media mavjud bo'lsa
        for image in product.product_media.all():
            with open(image.image.path, 'rb') as image_file:
                image_data = image_file.read()  # Fayl ma'lumotlarini bytes ob'ektiga o'girish

                if first_caption:
                    media.append(InputMediaPhoto(media=image_data, caption=product.text))
                    first_caption = False
                else:
                    media.append(InputMediaPhoto(media=image_data))

    return media if media else None



