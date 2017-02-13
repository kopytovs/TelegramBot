#! /usr/bin/env python
# -*- coding: utf-8 -*-
import config
import telebot
import random

bot = telebot.TeleBot(config.token)

help_text = 'Добро пожаловать в мой бот! Он может повторять ваши сообщения!'

mas = ['Орел', 'Решка', 'Ребро']

msg = 'кек'

markup = telebot.types.ReplyKeyboardMarkup()

markup.row('Помощь', '')

@bot.message_handler(commands=["help"])

def help_func(message):
    bot.send_message(message.chat.id, help_text)

#@bot.message_handler(commands=["stop"])

#def stop_bot():
    #bot.polling(none_stop=False)

@bot.message_handler(commands=["coin"])

def whoisInList(message):
    bot.send_message(message.chat.id, 'Кидаем монетку...')
    random.seed
    p = random.uniform(0,1)
    if (p > 0.5):
        msg = mas[0]
    elif (p < 0.5):
        msg = mas[1]
    elif (p == 0.5):
        msg = mas[2]
    bot.send_message(message.chat.id, msg)


@bot.message_handler(content_types=["text"])

def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
