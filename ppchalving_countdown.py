import requests
import time
from telegram import Bot
from telegram.error import TelegramError

token="6443464602:AAFOfUFkPyKALvvUhSCzTvy_OktvJxj94bo" #insert bot token here
channel="-1002008849502" #destination channel numeric id Ex. -100xxxxxxxxxxx

old = 0
block = 0
halvingBlock = 630000 + 210000
rocket = u'\U0001F680'
customMessage = "https://www.youtube.com/watch?v=PDJLvF1dUek"  # Text, url etc.

bot = Bot(token)

while block < (halvingBlock + 2):
    r = requests.get('https://blockchain.info/q/getblockcount')
    block = int(r.text)
    print(str(block))
    less = block - halvingBlock
    if old != block:
        if less < 0:
            txt = "Block " + str(block) + " mined!\n\n" + str(abs(less)) + " blocks to Halving!"
            print(txt)
            try:
                bot.send_message(chat_id=channel, text=txt, parse_mode='HTML')  # Send message
            except TelegramError as e:
                print("Error:\n" + str(e))
        if block == halvingBlock:
            txt = rocket * 5 + "\n\nBlock " + str(block) + " mined!\n\n Happy Halving!\n\n" + rocket * 6 + "\n\n" + customMessage
            try:
                bot.send_message(chat_id=channel, text=txt, parse_mode='HTML')  # Send message
            except TelegramError as e:
                print("Error:\n" + str(e))
    old = block
    time.sleep(abs(less) + 2)
