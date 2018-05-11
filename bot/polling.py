"""
Added a function to be able to recover from API network errors
"""
from telebot import TeleBot
from time import sleep
import logging

logging.basicConfig(level='DEBUG')

class Bot(TeleBot):
    def polling_enhanced(self):
        try:
            self.polling(none_stop=True, interval=0, timeout=5)
        except:
            self.stop_polling()
            sleep(10)
            self.polling_enhanced()