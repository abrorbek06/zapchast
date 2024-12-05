
from telebot import TeleBot

def set_webhook():
    """Set the webhook for the Telegram bot."""
    bot = TeleBot(token="7535576431:AAHBFnwqRpa2jfVpJlzGteS3CyVNLaA2FC0")

    # Set the webhook URL
    bot.remove_webhook()
    success = bot.set_webhook(url="https://c4cc-95-214-211-19.ngrok-free.app/blog/webhook/")

    if success:
        print(f"Webhook set successfully to ", bot.get_webhook_info())
    else:
        print("Failed to set webhook")

if __name__ == '__main__':
    set_webhook()
