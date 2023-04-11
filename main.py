import telebot
import requests

TOKEN = "Токен бота"
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    try:
        req = requests.get("http://127.0.0.1:5000/start")
        if req.ok:
            bot.send_message(text=req.text, chat_id=message.chat.id)
        else:
            bot.send_message(text="API.py не запущен!")
    except:
        bot.send_message(text="API.py не запущен!")


@bot.message_handler(commands=["stop"])
def stop(message):
    try:
        req = requests.get("http://127.0.0.1:5000/stop")
        if req.ok:
            bot.send_message(text=req.text, chat_id=message.chat.id)
        else:
            bot.send_message(text="API.py не запущен!")
    except:
        bot.send_message(text="API.py не запущен!")


bot.infinity_polling()
