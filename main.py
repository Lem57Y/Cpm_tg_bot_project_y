import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import API_TOKEN
from text import text1, text2, text3, text4, text5, text6, text7, text8, text9, text0, finaltext

keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
buttonN = KeyboardButton(text = "на север")
buttonS = KeyboardButton(text = "на юг")
buttonW = KeyboardButton(text = "на восток")
buttonE = KeyboardButton(text = "на запад")
buttonG = KeyboardButton(text = "открутить гайки")
buttonC = KeyboardButton(text = 'ввести код')
keyboard.add(buttonN)
keyboard.add(buttonS)
keyboard.add(buttonW)
keyboard.add(buttonE)
storage = {}
storage['des']= {}
storage['des'][0]= text0
storage['des'][1]= text1
storage['des'][2]= text2
storage['des'][3]= text3
storage['des'][4]= text4
storage['des'][5]= text5
storage['des'][6]= text6
storage['des'][7]= text7
storage['des'][8]= text8
storage['des'][9]= text9


bot = telebot.TeleBot(API_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    global storage
    global keyboard
    iD = message.from_user.id
    first_text = text1


    bot.send_message(
        message.chat.id,
        first_text,
        reply_markup=keyboard
    )
    storage[iD] = {"room": 1, 'key': 0, 'code': 0, 'wrench': 0, 'unlock': 0, 'rooms': {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}}
    
    
    


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    global keyboard
    global storage
    text = message.text
    iD = message.from_user.id
    room = storage[iD]["room"]


    if len(text) == 10 and room == 5:
        if text == '1819991218':
            storage[iD]['code'] = 1
            bot.send_message(
                message.from_user.id,
                'код верный, дверь разблокирована',
            )

    if room != 5 or room != 0:
        keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
        keyboard.add(buttonN)
        keyboard.add(buttonS)
        keyboard.add(buttonW)
        keyboard.add(buttonE)


    if text == 'описание':
        bot.send_message(
            message.from_user.id,
            storage['des'][room]
        )
         
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

        if text == 'на север':
            if storage[iD]['code'] == 1:
                storage[iD]["room"] = 0
                bot.send_message(
                    message.from_user.id,
                    'вы прошли через дверь ' + text,
                )

               
            else:
                bot.send_message(
                    message.from_user.id,
                    'дверь заблокирована необходимо ввести код',
                )

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

    elif room == 0:
        if text == "на юг":
            bot.send_message(
                message.from_user.id,
                'вы прошли через дверь ' + text,
            )
            storage[iD]["room"] = 5

    print(storage[iD]["room"])
    room = storage[iD]["room"]

    
    if storage[iD]["rooms"][room] == 0:
        bot.send_message(
            message.from_user.id,
            storage["des"][room],
        )
        storage[iD]["rooms"][room] = 1


    
    if room == 2:
        storage[iD]['key'] = 1

    if room == 5:
        if text == 'ввести код':
            bot.send_message(
                message.from_user.id,
                'напишите код (слейдушее сообщение это код без пробелов)',
            )
        elif storage[iD]['code'] == 0:
            keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
            keyboard.add(buttonN)
            keyboard.add(buttonS)
            keyboard.add(buttonW)
            keyboard.add(buttonE)
            keyboard.add(buttonC)
            bot.send_message(
                message.from_user.id,
                '...',
                reply_markup=keyboard,
            )

    if room == 0:
        if text == 'открутить гайки':
            bot.send_message(
                message.from_user.id,
                finaltext,
            )
            storage[iD]['unlock'] = 1

        if storage[iD]['unlock'] == 0:
            keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
            keyboard.add(buttonN)
            keyboard.add(buttonS)
            keyboard.add(buttonW)
            keyboard.add(buttonE)
            keyboard.add(buttonG)
            bot.send_message(
                message.from_user.id,
                '...',
                reply_markup=keyboard,
            )


    if room == 7:
        storage[iD]['wrench'] = 1

    if room == 3:
        storage[iD] = {}
        storage[iD] = {"room": 1, 'key': 0, 'code': 0, 'wrench': 0, 'unlock': 0, 'rooms': {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}}

        


    

  

    storage[iD]['rooms'][room] = 1


        
        



    

bot.infinity_polling()