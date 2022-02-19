import os
import telegram
from time import sleep
from spacex import fetch_spacex_last_launch
from nasa import get_nasa_images, get_extension
from epic import get_epic_images
from time import sleep
from dotenv import load_dotenv
from pprint import pprint


def get_images(spacex_url, spacex_path, nasa_url, nasa_path, last_date_epic_url, epic_path, nasa_api_key):
    images_path = []
    spacex_images_path = fetch_spacex_last_launch(spacex_url, spacex_path)
    nasa_images_path = get_nasa_images(nasa_url, nasa_path)
    epic_images_path = get_epic_images(last_date_epic_url, epic_path, nasa_api_key)
    images_path.extend(spacex_images_path)
    images_path.extend(nasa_images_path)
    images_path.extend(epic_images_path)
    return images_path

def telegram_bot(telegram_token, chat_id, images_path):   #Название
    bot = telegram.Bot(telegram_token)
    bot.send_message(chat_id=chat_id, text="Hello!")
    for image_path in images_path:
        with open(image_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
    bot.send_message(chat_id=chat_id, text="Goodbye!")


if __name__ == "__main__":
    load_dotenv()
    
    nasa_path = "../nasa_photos"
    spacex_path = "../spacex_photos"
    epic_path = "../epic_photos"
    
    delay_time = os.environ['DELAY_TIME']
    nasa_api_key = os.environ['NASA_API_KEY']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']


    while True:
        images_path = get_images(spacex_url, spacex_path, nasa_url, nasa_path, last_date_epic_url, epic_path, nasa_api_key)
        telegram_bot(telegram_token, chat_id, images_path)
        print("ok")
        sleep(86400)
