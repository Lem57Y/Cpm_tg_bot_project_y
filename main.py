import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import API_TOKEN

keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
button = KeyboardButton(text = "на север")
button1 = KeyboardButton(text = "на юг")
button2 = KeyboardButton(text = "на восток")
button3 = KeyboardButton(text = "на запад")
button4 = KeyboardButton(text = "счётчик гейгера")
keyboard.add(button)
keyboard.add(button1)
keyboard.add(button2)
keyboard.add(button3)
storage = {}



bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])




def send_welcome(message):
    global storage
    iD = message.from_user.id
    first_text = ("Hello") + (' ') + message.from_user.first_name + (' ') + ('@') + message.from_user.username
    #keyboard = ReplyKeyboardMarkup()
    #keyboard.add(button)
    bot.send_message(
        message.chat.id,
        first_text,
        reply_markup=keyboard
    )
    storage[iD] = {"room": 1, 'key': 1, 'code': 0, 'rooms': {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}}
    
    
    


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    global storage
    text = message.text
    iD = message.from_user.id
    room = storage[iD]["room"]

    if room == 1:
        if text == 'на север':
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 4
            

    elif room == 2:
        if text == "на север":
            bot.send_message(
                message.from_user.id,
                'Вы прошли через пролом в стене ' + text,
            )
            storage[iD]["room"] = 8

        elif text == "на запад":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 3

    elif room == 4:
        if text == "на север":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 6

        elif text == "на юг":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 1

        elif text == "на восток":
            if storage[iD]['key'] == 1:
                bot.send_message(
                message.from_user.id,
                'вы отрыли дверь ключ-картой и прошли ' + text,
                )
                storage[iD]["room"] = 5

            else:
                bot.send_message(
                    message.from_user.id,
                    'необходима ключ-карта'
                )


    elif room == 5:
        if text == "на запад":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 4

    elif room == 6:
        if text == "на север":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 7
        
        elif text == "на запад":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 8

        elif text == "на юг":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 4

    elif room == 7:
        if text == "на юг":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 6

    elif room == 8:
        if text == "на восток":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 6

        elif text == "на запад":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 9

        elif text == "на юг":
            bot.send_message(
                message.from_user.id,
                'вы прошли через пролом в стене ' + text,
            )
            storage[iD]["room"] = 2

    elif room == 9:
        if text == "на восток":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 8

        if text == "на юг":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 3

    print(storage[iD]["room"])


        
        



    

bot.infinity_polling()