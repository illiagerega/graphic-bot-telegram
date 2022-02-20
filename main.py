import telebot
from telebot import types

import config
import stats_

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
import os

bot = telebot.TeleBot(config.key)

global state
state = ''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global keyboardmain

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    cycle_stat = types.InlineKeyboardButton(text='Кругова діаграма', callback_data='cycle_stat')
    stat = types.InlineKeyboardButton(text='Звичаний графік', callback_data='stat')
    klitor_stat = types.InlineKeyboardButton(text='Графік-кліматограма', callback_data='klitor_stat')
    price_stat = types.InlineKeyboardButton(text='Визначення рівноважної ціни', callback_data='price_stat')
    keyboard.add(cycle_stat, stat, klitor_stat, price_stat)

    bot.send_message(message.chat.id, 'Головне меню', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global state
    if call.data == 'menu':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        cycle_stat = types.InlineKeyboardButton(text='Кругова діаграма', callback_data='cycle_stat')
        stat = types.InlineKeyboardButton(text='Звичаний графік', callback_data='stat')
        klitor_stat = types.InlineKeyboardButton(text='Графік-кліматограма', callback_data='klitor_stat')
        price_stat = types.InlineKeyboardButton(text='Визначення рівноважної ціни', callback_data='price_stat')
        keyboard.add(cycle_stat, stat, klitor_stat, price_stat)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Головне меню',
                              reply_markup=keyboard)

    if call.data == 'cycle_stat':
        state = 'cycle_stat'
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        backbutton = types.InlineKeyboardButton(text='⬅️Назад', callback_data='menu')
        keyboard.add(backbutton)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Напишіть дані для опрацювання. Приклад: a 1 b 2 c 3', reply_markup=keyboard)

    if call.data == 'stat':
        state = 'stat'
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        backbutton = types.InlineKeyboardButton(text='⬅️Назад', callback_data='menu')
        keyboard.add(backbutton)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Напишіть дані для опрацювання. Приклад: a 1 b 2 c 3', reply_markup=keyboard)

    if call.data == 'klitor_stat':
        state = 'klitor_stat'
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        backbutton = types.InlineKeyboardButton(text='⬅️Назад', callback_data='menu')
        keyboard.add(backbutton)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Напишіть дані для опрацювання. Приклад: a 1 b 2 c 3', reply_markup=keyboard)

    if call.data == 'price_stat':
        state = 'price_stat'
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        backbutton = types.InlineKeyboardButton(text='⬅️Назад', callback_data='menu')
        keyboard.add(backbutton)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Напишіть дані для опрацювання. Приклад: a 1 2 b 2 4 c 2 7', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if state == 'cycle_stat':
        print('cycle_stat')

        message_text = message.text 
        data = message_text.split()

        labels = []
        numbers = []

        if len(data) % 2 == 0:
 
            for i in data:
                if i.isnumeric():
                    numbers.append(i)
                else:
                    labels.append(i)

            font = {'family': 'Verdana', 'weight': 'normal'}
            rc('font', **font)
        
            y = np.array(numbers)
        
            plt.pie(y, labels = labels)
            #plt.show()
            if os.path.isfile('foo.png'):
                os.remove('foo.png')
                plt.savefig('foo.png')
                plt.close()
            else:
                plt.savefig('foo.png')
                plt.close()

            bot.send_photo(chat_id=message.chat.id, photo=open('foo.png', 'rb'))
            
            print(message_text)

        else:
            print('dont coreect')

    if state == 'stat':
        print('stat')
        message_text = message.text 
        data = message_text.split()

        labels = []
        numbers = []

        if len(data) % 2 == 0:
 
            for i in data:
                if i.isnumeric():
                    numbers.append(i)
                else:
                    labels.append(i)

            plt.plot(labels, numbers)
            #plt.show()
            if os.path.isfile('foo.png'):
                os.remove('foo.png')
                plt.savefig('foo.png')
                plt.close()
            else:
                plt.savefig('foo.png')
                plt.close()

            bot.send_photo(chat_id=message.chat.id, photo=open('foo.png', 'rb'))
            
            print(message_text)

        else:
            print('dont coreect')

    if state == 'klitor_stat':
        print('stat')
        message_text = message.text 
        data = message_text.split()

        labels = []
        numbers = []

        if len(data) % 2 == 0:
 
            for i in data:
                if i.isnumeric():
                    numbers.append(i)
                else:
                    labels.append(i)

            plt.bar(labels, numbers)
            #plt.show()
            if os.path.isfile('foo.png'):
                os.remove('foo.png')
                plt.savefig('foo.png')
                plt.close()
            else:
                plt.savefig('foo.png')
                plt.close()

            bot.send_photo(chat_id=message.chat.id, photo=open('foo.png', 'rb'))
            
            print(message_text)

        else:
            print('dont coreect')


    if state == 'price_stat':
        print('stat')
        message_text = message.text 
        data = message_text.split()

        labels = []
        numbers_1 = []
        numbers_2 = []

        if len(data) % 3 == 0:
 
            for i in data:
                if i.isnumeric():
                    if len(numbers_1) < len(numbers_2):
                        numbers_1.append(i)
                    else:
                        numbers_2.append(i)
                else:
                    labels.append(i)

            stats_.price_stat(labels, labels, numbers_1, numbers_2)

            plt.plot(labels, numbers_1)
            plt.plot(labels, numbers_2)

            plt.legend()

            #plt.show()
            if os.path.isfile('foo.png'):
                os.remove('foo.png')
                plt.savefig('foo.png')
                plt.close()
            else:
                plt.savefig('foo.png')
                plt.close()

            bot.send_photo(chat_id=message.chat.id, photo=open('foo.png', 'rb'))
            
            print(message_text)

        else:
            print('dont coreect')



# for test
if __name__ == '__main__':
    bot.polling(none_stop=True)


# for production
# while True:
#    try:
#        bot.polling(none_stop=True, interval=0, timeout=0)
#    except:
#        time.sleep(10)
