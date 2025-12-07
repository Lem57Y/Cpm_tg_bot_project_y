import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import API_TOKEN

keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
button = KeyboardButton(text = "Left")
button1 = KeyboardButton(text = "Right")
button2 = KeyboardButton(text = "Restart")
keyboard.add(button)
keyboard.add(button1)
keyboard.add(button2)
room = 0




bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])

def send_welcome(message):
    global room
    first_text = ("Hello") + (' ') + message.from_user.first_name + (' ') + ('@') + message.from_user.username
    bot.send_message(
        message.chat.id,
        first_text,
        reply_markup=keyboard)
    room = 1
    


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    global room
    text = message.text
    if text == "Restart": 
        bot.send_message(
            message.from_user.id,
            'The game has been restarted',
        )
        room = 1
    else:
        if room == 1:
            if text == "Left":
                bot.send_message(
                    message.from_user.id,
                    'You went left from room' + str(room),
                )
                room = 2

            elif text == "Right":
                bot.send_message(
                    message.from_user.id,
                    'You went right from room' + str(room),
                )
                room = 3
                
            else:
                bot.send_message(
                    message.from_user.id,
                    "You presed someting wrong",
                )

    
        elif room == 2:
            if text == "Left":
                bot.send_message(
                    message.from_user.id,
                    'You went left from room' + str(room),
                )
                room = 4

            elif text == "Right":
                bot.send_message(
                    message.from_user.id,
                    'You went right from room' + str(room),
                )
                room = 1
                
            else:
                bot.send_message(
                    message.from_user.id,
                    "You presed someting wrong",
                )


        elif room == 3:
            if text == "Left":
                bot.send_message(
                    message.from_user.id,
                    'You went left from room' + str(room),
                )
                room = 5

            elif text == "Right":
                bot.send_message(
                    message.from_user.id,
                    'You went right from room' + str(room),
                )
                room = 1
                
            else:
                bot.send_message(
                    message.from_user.id,
                    "You presed someting wrong",
                )


        elif room == 4:
            if text == "Left":
                bot.send_message(
                    message.from_user.id,
                    'You went left from room' + str(room),
                )
                room = 3

            elif text == "Right":
                bot.send_message(
                    message.from_user.id,
                    'You went right from room' + str(room),
                )
                room = 2
                
            else:
                bot.send_message(
                    message.from_user.id,
                    "You presed someting wrong",
                )        


        if room == 5:
            bot.send_message(
                    message.from_user.id,
                    "Congratulations, you escaped.",
                )  
            bot.send_message(
                    message.from_user.id,
                    "if you want to play again, press restart",
                )  
    

bot.infinity_polling()