from bot_logic import gen_pass
from bot_logic import em
from bot_logic import a
import telebot
import random 

bot = telebot.TeleBot("8634225792:AAFbriQ5MhkwKABdyI_r9kOSBtePTnSRXFo")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!(/help для каталога команд)")
    

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['parol'])
def send_password(message):
    password = gen_pass(10)
    bot.send_message(message.chat.id, f"Рандомный пароль: {password}")
    

# Send a reactions to all messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=["gen_emodsi"])
def send_reaction(message):
    qqq = em()
    bot.send_message(message.chat.id, f"Рандомный смайл: {qqq}")

    
@bot.message_handler(commands=["help"])
def send_reaction(message):
    bot.reply_to(message, "/start - запуск бота | /hello и /bye - команды просто просто поговорить) | /parol - вам нужен пароль? Бот просто сгенерирует тебе пароль | /gen_emodsi - рандомный смайлик для поднятия настроения | /anekdot - рандомный анекдот, тоже для поднятия настроения)")


@bot.message_handler(commands=["anekdot"])
def anekdot(message):
    anek = a()
    bot.send_message(message.chat.id, f"Рандомный анекдот: {anek}")



@bot.message_handler(func = lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я тебя не понимаю! Напиши /help, если нужен каталог команд!")



bot.polling()
