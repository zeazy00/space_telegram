import logging
import os
import requests
from common import download_image

logging.basicConfig(level=logging.INFO)

def get_epic_images(nasa_api_key, epic_path="../epic_photos"):
    params = {"api_key": nasa_api_key}
    last_date_epic_url = f"https://api.nasa.gov/EPIC/api/natural"
    number_of_pictures = 0
    epic_images_path = []
    response = requests.get(last_date_epic_url, params)
    response.raise_for_status()
    images_info = response.json()
    os.makedirs(epic_path, exist_ok=True)
    for image_info in images_info:
        photo_date = image_info["date"].replace("-", "/").split()[0]
        filename = f'{image_info["image"]}.png'
        epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{filename}'
        os.makedirs(epic_path, exist_ok=True)
        download_image(filename, epic_path, epic_photo_url, params)
        epic_images_path.append(f"{epic_path}/{filename}")
        number_of_pictures = number_of_pictures + 1
    logging.info(f"images from EPIC: {number_of_pictures}")
    return epic_images_path
