import telebot
import os
import requests
from flask import Flask, request

# Отримання токена і URL вебхука з середовища
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Обробка /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("📗 Інструкція", url="https://t.me/..."))
    markup.add(telebot.types.InlineKeyboardButton("📞 Підтримка", url="https://t.me/..."))
    markup.add(telebot.types.InlineKeyboardButton("📈 Платформа", url="https://..."))
    bot.send_message(message.chat.id, "👋 Привіт! Ти потрапив до бота, де я розповідаю, як заробляю з телефону 📱", reply_markup=markup)

# Вебхук endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200

# Для перевірки, що бот живий
@app.route("/", methods=["GET"])
def index():
    return "Bot is running."

# Запуск + установка вебхука
if __name__ == "__main__":
    if WEBHOOK_URL:
        set_hook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}"
        requests.get(set_hook_url)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
