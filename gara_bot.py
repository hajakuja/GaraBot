import telebot  
import settings
import os
import json
from datetime import datetime

bot = telebot.TeleBot('820621103:AAFQuMe981BfPUzYFhTrEHnLkgPiNqAkkK4')


@bot.message_handler(commands=['start', 'help'])
def initial(message):
    if not os.path.exists('data/data.json'):
        os.mkdir('data')
        with open('data/data.json', 'w') as data_file:
            dct = {'date':str(datetime.now()) } 
            json.dump(dct, data_file)
    bot.reply_to(message, "Hi!")




# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
# bot.polling()  

      


@bot.message_handler(func=lambda m: m.text in settings.ACC_MESSAGES)
def count_save(message):
    who = message.from_user
    
    f = open("data/data.json",'r')
    data_json = json.load(f)
    f.close()
    
    # print("The original json data type : {}\n".format(type(data_json)))
    
    if str(who.id) in data_json:
        data_json[str(who.id)]['count'] += 1
        data_json[str(who.id)]['count'].append(str(datetime.now()))
    else:
        data_json[who.id] = {'name':who.first_name, 'count':1, 'entry_dates':[str(datetime.now())]}

    with open('data/data.json', 'w') as data_file:
        json.dump(data_json, data_file)
    
    
bot.polling()


