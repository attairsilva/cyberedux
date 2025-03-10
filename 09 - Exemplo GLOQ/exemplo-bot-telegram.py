import os
from dotenv import load_dotenv
load_dotenv() 
#------------------------------------------------

import telebot

bot = telebot.TeleBot("Seu token do telegram")
# bot = telebot.TeleBot(os.getenv('TOKEN_BOT_TELEGRAM'))

@bot.message_handler(commands=['start'])#, 'help'])
def mensagem_inicial(message):
    dict_nome = bot.get_my_name()
    nome = dict_nome.name
    bot.reply_to(message, f'Ola! Sou seu bot {nome}')

@bot.message_handler(commands=['sair'])
def sair(message):
    bot.reply_to(message, 'Ok, :(')
    bot.stop_polling()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# roda o TeleBot
bot.polling()
