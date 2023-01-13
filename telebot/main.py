from token_bot import token
import telebot
from telebot import types
from raspisanie import df101,dk101,dl101,dp101,dis102,dgd101
from raspisanie import dis202,db201,dk201,dp201,df201,dl201,dis203
from raspisanie import dk301,db301,di301,di302,dp301,dp302 ,df301



bot = telebot.TeleBot(token)

@bot.message_handler(commands =['start'])   
def start(message):
    try:
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Наша группа", url='https://t.me/+Wm38cFqHWqE1YmUy')
        markup.add(button1)
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди в нашу общую группу телеграмм)".format(message.from_user), reply_markup=markup)
        markup2 =  types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("1 курс")
        btn1 = types.KeyboardButton("2 курс")
        btn2 = types.KeyboardButton("3 курс")
        markup2.add(btn,btn1,btn2)
        bot.send_message(message.chat.id, text = "Выберите вашу группу:".format(message.from_user), reply_markup=markup2)
    except Exception as ex:
        print(ex)
@bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text == "ДИС-301"):
#         bot.send_message(message.chat.id, text= ras1)
#     elif(message.text == "ДФ-101"):
#         bot.send_message(message.chat.id, text= ras2)
#     elif(message.text == "ДК-101"):
#         bot.send_message(message.chat.id, text= ras3)
#     elif(message.text == "ДЛ-101"):
#         bot.send_message(message.chat.id, text= ras4)
#     elif(message.text == "ДП-101"):
#         bot.send_message(message.chat.id, text= ras5)
#     elif(message.text == "ДИС-102"):
#         bot.send_message(message.chat.id, text= ras6)
#     elif(message.text == "ДГД-101"):
#         bot.send_message(message.chat.id, text=ras7)
#     elif(message.text == "ДИС-202"):
#         bot.send_message(message.chat.id, text=ras8)
#     elif(message.text == "ДК-201"):
#         bot.send_message(message.chat.id, text=ras9)
#     elif(message.text == "ДП-201"):
#         bot.send_message(message.chat.id, text=ras10)
#     elif(message.text == "ДФ-201"):
#         bot.send_message(message.chat.id, text=ras11)
#     elif(message.text == "ДЛ-201"):
#         bot.send_message(message.chat.id, text=ras12)
#     elif(message.text == "ДИС-203"):
#         bot.send_message(message.chat.id, text=ras13)
#     elif(message.text == "ДК-301"):
#         bot.send_message(message.chat.id, text=ras14)
#     elif(message.text == "ДБ-301"):
#         bot.send_message(message.chat.id, text=ras15)
#     elif(message.text == "ДИ-301"):
#         bot.send_message(message.chat.id, text=ras16)
#     elif(message.text == "ДИ-302"):
#         bot.send_message(message.chat.id, text=ras17)
#     elif(message.text == "ДП-301"):
#         bot.send_message(message.chat.id, text=ras18)
#     elif(message.text == "ДП-302"):
#         bot.send_message(message.chat.id, text=ras19)
#     elif(message.text == "ДФ-301"):
#         bot.send_message(message.chat.id, text=ras20)
#     elif(message.text == "ДИ-401"):
#         bot.send_message(message.chat.id, text=ras21)
@bot.message_handler(content_types=['1 курс'])
def first_course(message):
    #df101,dk101,dl101,dp101,dis102,dgd101
    bot.send_message(message.chat.id, text="1 курс)")
    markup =  types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ДФ-101")
    btn2 = types.KeyboardButton("ДК-101")
    btn3 = types.KeyboardButton("ДЛ-101")
    btn4 = types.KeyboardButton("ДП-101")
    btn5 = types.KeyboardButton("ДИС-102")
    btn6 = types.KeyboardButton("ДГД-101")
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
@bot.message_handler(content_types=['text'])
def second_year(message):
    #dis202,db201,dk201,dp201,df201,dl201,dis203
    bot.send_message(message.chat.id, text="2 курс)")
@bot.message_handler(content_types=['text'])
def third_year(message):
    #dk301,db301,di301,di302,dp301,dp302 ,df301
    bot.send_message(message.chat.id, text="2 курс)")

bot.polling(none_stop = True)
