import json
import os

import django
import telebot
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from example_app.botapp.core.loader import bot, middlewares

import example_app.botapp.handlers


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homeidea.settings')
django.setup()

middlewares()

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update_data = json.loads(request.body.decode('UTF-8'))
        update = telebot.types.Update.de_json(update_data)
        bot.process_new_updates([update])
        return JsonResponse({"status": "ok"})