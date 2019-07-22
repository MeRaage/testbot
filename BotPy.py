import telebot
import time, threading
import requests
from bs4 import BeautifulSoup
import time, threading
import shelve
userid=344017358
sendbool = False
global Timebool
global textinfo
ListUsers=list()
bot = telebot.TeleBot('590740321:AAGkPd-AWnYNuy16T-34sP4iHzXF55U0pbc');
ListCommand = [
              ["/list","You'll can see my anime list "],
              ["/favorite","My lovely anime"]
]


def SendInfo():
        bot.send_message(344017358,"Hello",disable_web_page_preview=True)


@bot.message_handler(commands=['help','start'])
def get_text_messages2(message):
    if message.text =='/start':
        bot.send_message(message.from_user.id, "Спасибо за регистрацию вы получите уведомление о новых сериях!!!")
    #if message.text =='/help':
    #    bot.send_message(message.from_user.id, AllCommand())

def SendInfo(item):
    bot.send_message(344017358, item)
#import threading

#def writer(x, event_for_wait, event_for_set):
        #event_for_wait.wait() # wait for event
    #event_for_wait.clear() # clean event for future
        #print(x)
    #    event_for_set.set() # set event for neighbor thread

# init events
#event1 = threading.Event()
#event2 = threading.Event()

# init threads

#t1 = threading.Thread(target=writer, args=(0, event1, event2))
#t2 = threading.Thread(target=writer, args=(1, event2, event1))

# start threads
#t1.start()
#t2.start()

#event1.set() # initiate the first event

# join threads to the main thread
#t1.join()
#t2.join()
threading.Thread(target=bot.polling).start()
if __name__ == '_main_':
    main()
