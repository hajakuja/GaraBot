import telebot  
import settings
import os
import json
import helpers
from datetime import datetime

bot = telebot.TeleBot('820621103:AAFQuMe981BfPUzYFhTrEHnLkgPiNqAkkK4')


@bot.message_handler(commands=['start'])
def initial(message):
    bot.reply_to(message, "Hi!")

      
@bot.message_handler(func=lambda m: m.text in settings.ACC_MESSAGES)
def count_save(message):
    who = message.from_user
    data_json = {}
    if os.path.exists(settings.DATA_PATH):
        f = helpers.open_data_file('r')
        data_json = json.load(f)
        f.close()
        if str(who.id) in data_json:
            data_json[str(who.id)]['count'] += 1
            data_json[str(who.id)]['entry_dates'].append(str(datetime.now()))
        else:
            data_json[who.id] = {'name':who.first_name, 'count':1, 'entry_dates':[str(datetime.now())]}

    else:
        os.mkdir(settings.DATA_DIR)
        data_json[who.id] = {'name':who.first_name, 'count':1, 'entry_dates':[str(datetime.now())]}
    

    with open('data/data.json', 'w') as data_file:
        json.dump(data_json, data_file)

@bot.message_handler(commands=['lista'])
def reply_lista(message):

    f = helpers.open_data_file('r')
    if f is None:
        bot.reply_to(message, "Nuk ka te dhena!")
        return

    data_json = json.load(f)
    f.close()
    msg = ''
    for i in data_json:
        name = data_json[i]['name']
        count = data_json[i]['count']

        msg += '{} : {} \n'.format(data_json[i]['name'], data_json[i]['count'])   
    bot.reply_to(message, msg)


bot.polling()



