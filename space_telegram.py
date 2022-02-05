import os
import requests
import tg
from time import sleep
from dotenv import load_dotenv
from urllib.parse import urlparse
from pprint import pprint
from pathvalidate import sanitize_filename

load_dotenv()

nasa_path = "nasa_photos"
spacex_path = "spacex_photos"
epic_path = "epic_photos"

nasa_api_key = os.environ['NASA_API_KEY']
telegram_token = os.environ['TELEGRAM_TOKEN']
chat_id = os.environ['CHAT_ID']

nasa_url = f"https://api.nasa.gov/planetary/apod?count=30&api_key={nasa_api_key}"
spacex_url = "https://api.spacexdata.com/v4/launches/latest"
last_date_epic_url = f"https://api.nasa.gov/EPIC/api/natural?api_key={nasa_api_key}"


def fetch_spacex_last_launch(spacex_url, spacex_path):
	spacex_images_path = []
	response = requests.get(spacex_url)
	response.raise_for_status()
	links = response.json()["links"]["flickr"]["original"]
	if (links == []):
		print("no spasex links")
	else:
		for link in enumerate(links):
			filename = f"spacex{link[0]+1}.jpg"
			print("1)", spacex_path, "2)", filename, "3)", link[1])
			get_image(filename, spacex_path, link[1])
			spacex_images_path.append(f"{spacex_path}/{filename}")
	return spacex_images_path


def get_nasa_images(nasa_url, nasa_path):
	nasa_images_path = []
	response = requests.get(nasa_url)
	response.raise_for_status()
	images_info = response.json()
	for image_info in images_info:
		if 'hdurl' in image_info:
			filename = sanitize_filename(image_info['title'] + get_extension(image_info['hdurl']))
			get_image(filename, nasa_path, image_info['hdurl'])
			print("1)", nasa_path, "2)", filename, "3)", image_info['hdurl'])
			nasa_images_path.append(f"{nasa_path}/{filename}")
		else:
			print("1)", nasa_path, image_info["date"], "error")
	return nasa_images_path


def get_epic_images(last_date_epic_url, epic_path, nasa_api_key):
	epic_images_path = []
	response = requests.get(last_date_epic_url)
	response.raise_for_status()
	images_info = response.json()
	for image_info in images_info:
		epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_info["date"].replace("-", "/").split()[0]}/png/{image_info["image"]}.png?api_key={nasa_api_key}'
		filename = f'{image_info["image"]}.png'
		get_image(filename, epic_path, epic_photo_url)
		print("1)", epic_path, "2)", filename, "3)", epic_photo_url, "\n", image_info["date"])
		epic_images_path.append(f"{epic_path}/{filename}")
	return epic_images_path 


def get_extension(url):
	file_path = urlparse(url)
	extension = os.path.splitext(file_path.path)[1]
	return extension 

	 
def get_image(filename, path, url):
	os.makedirs(path, exist_ok=True)

	response = requests.get(url)
	response.raise_for_status()

	file_path = f"{path}/{filename}"

	with open(file_path, 'wb') as file:
		file.write(response.content)


def get_images(spacex_url, spacex_path, nasa_url, nasa_path, last_date_epic_url, epic_path, nasa_api_key):
	images_path = []
	spacex_images_path = fetch_spacex_last_launch(spacex_url, spacex_path)
	nasa_images_path = get_nasa_images(nasa_url, nasa_path)
	epic_images_path = get_epic_images(last_date_epic_url, epic_path, nasa_api_key)
	images_path.extend(spacex_images_path)
	images_path.extend(nasa_images_path)
	images_path.extend(epic_images_path)
	return images_path

def telegram_bot(telegram_token, chat_id, images_path):
	text = "hi"
	bot = tg.tg_bot_start(telegram_token)
	tg.tg_send_message(bot, chat_id, text)
	tg.tg_send_photo(bot, chat_id, images_path)
	tg_send_message(bot, chat_id, text)


if __name__ == "__main__":
	while True:
		images_path = get_images(spacex_url, spacex_path, nasa_url, nasa_path, last_date_epic_url, epic_path, nasa_api_key)
		telegram_bot(telegram_token, chat_id, images_path)
		print("ok")
		sleep(86400)



	#cd C:\Users\Zeazy\Desktop\something\time\python\devman\space_telegram