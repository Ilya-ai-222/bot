from bot_logic import gen_pass
from bot_logic import em
import telebot
import random 


bot = telebot.TeleBot("8634225792:AAFbriQ5MhkwKABdyI_r9kOSBtePTnSRXFo")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['gen password'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))
    

# Send a reactions to all messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=["gen emo"])
def send_reaction(message):
    bot.reply_to(message, em())



@bot.message_handler(func = lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()