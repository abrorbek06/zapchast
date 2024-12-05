
from telebot import TeleBot




def set_webhook():
    """Set the webhook for the Telegram bot."""
    bot = TeleBot(token="7726096165:AAFkxjHTpH68V1lIo8iCXpPwlX3Zs5eJ6FM")

    # Set the webhook URL
    bot.remove_webhook()
    success = bot.set_webhook(url="https://633a-95-214-211-26.ngrok-free.app/blog/webhook/")

    if success:
        print(f"Webhook set successfully to ", bot.get_webhook_info())
    else:
        print("Failed to set webhook")

if __name__ == '__main__':
    set_webhook()
