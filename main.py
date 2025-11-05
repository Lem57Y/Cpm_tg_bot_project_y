import telebot
from telebot.types import Message
from config import API_TOKEN
API_TOKEN = '8225226157:AAGzbrjXBOZFfZnWYJtpzfgMXF15qMt0BWI'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    first_text = ("Hello") + (' ') + message.from_user.first_name + (' ') + ('@') + message.from_user.username
    bot.reply_to(message, first_text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    text = message.text
    word_count = ('Number of words: ') + str(text.count(" ") + 1)
    sumbol_count = ('Number of sumbols: ') + str(len(text))
    new_text = word_count + ('\n') + sumbol_count
    bot.reply_to(message, new_text)

bot.infinity_polling()