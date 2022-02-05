import telegram
from time import sleep

def tg_bot_start(telegram_token):
    bot = telegram.Bot(telegram_token)
    print(bot)
    return(bot)

def tg_send_message(bot, chat_id, input_text):
    bot.send_message(chat_id=chat_id, text=input_text)

def tg_send_photo(bot, chat_id, images):
    for image in images:
        bot.send_document(chat_id=chat_id, document=open(image, 'rb'))
        sleep(5)
