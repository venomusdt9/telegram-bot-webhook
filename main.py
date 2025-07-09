import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🔰 Інструкція", url="https://t.me/..."))
    markup.add(telebot.types.InlineKeyboardButton("📞 Підтримка", url="https://t.me/..."))
    markup.add(telebot.types.InlineKeyboardButton("📈 Платформа", url="https://..."))
    bot.send_message(message.chat.id, "👋 Привіт! Ти потрапив до бота, де я розповідаю, як заробляю з телефону 💸", reply_markup=markup)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
