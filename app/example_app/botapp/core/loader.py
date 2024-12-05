
from telebot import TeleBot, custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand

BOT_TOKEN = "7535576431:AAHBFnwqRpa2jfVpJlzGteS3CyVNLaA2FC0"
state_storage = StateMemoryStorage()

bot = TeleBot(
    token=BOT_TOKEN,
    threaded=False,
    use_class_middlewares=True,
    state_storage=state_storage,
)

bot.set_my_commands(commands=[
    BotCommand("/start", "Restart 🚀")
])

bot.add_custom_filter(custom_filter=custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filter=custom_filters.ChatFilter())


def middlewares():
    from telebot.handler_backends import BaseMiddleware
    from telebot.handler_backends import CancelUpdate

    class SimpleMiddleware(BaseMiddleware):
        def __init__(self, limit) -> None:
            super().__init__()
            self.last_time = {}
            self.limit = limit
            self.update_types = ['message']

        def pre_process(self, message, data):
            if not message.from_user.id in self.last_time:
                self.last_time[message.from_user.id] = message.date
                return
            if message.date - self.last_time[message.from_user.id] < self.limit:

                bot.send_message(message.chat.id, "Siz oz muddat ichida ko'p so'rov amalga oshirayapsiz❗️\nIltimos kuting!")
                return CancelUpdate()
            self.last_time[message.from_user.id] = message.date

        def post_process(self, message, data, exception):
            pass
