import os
import random
import telegram
from time import sleep
from spacex import fetch_spacex_last_launch
from apod import get_apod_images, get_extension
from epic import get_epic_images
from time import sleep
from dotenv import load_dotenv
from pprint import pprint


def download_images(nasa_api_key):
    images_path = []
    spacex_images_path = fetch_spacex_last_launch()
    apod_images_path = get_apod_images(nasa_api_key)
    epic_images_path = get_epic_images(nasa_api_key)
    images_path.extend(spacex_images_path)
    images_path.extend(apod_images_path)
    images_path.extend(epic_images_path)
    return images_path


def send_images(telegram_token, chat_id, images_path, delay_time):
    bot = telegram.Bot(telegram_token)
    bot.send_message(chat_id=chat_id, text="Hello!")
    for image_path in images_path:
        with open(image_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
        sleep(delay_time)
    bot.send_message(chat_id=chat_id, text="Goodbye!")
    return bot


if __name__ == "__main__":
    load_dotenv()
    delay_time = float(os.environ['DELAY_TIME'])
    nasa_api_key = os.environ['NASA_API_KEY']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']

    while True:
        images_path = download_images(nasa_api_key)
        bot = send_images(telegram_token, chat_id, images_path, delay_time)
        print(bot)
        print("ok")
        sleep(86400)
