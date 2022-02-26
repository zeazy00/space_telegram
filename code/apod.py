import os
import requests
from common import get_image
from pathvalidate import sanitize_filename
from urllib.parse import urlparse

number_of_pictures = 0
errors = 0


def get_apod_images(nasa_path):
    nasa_url = f"https://api.nasa.gov/planetary/apod?count=30&api_key={nasa_api_key}"
    nasa_images_path = []
    response = requests.get(nasa_url)
    response.raise_for_status()
    images_info = response.json()
    for image_info in images_info:
        if 'hdurl' in image_info:
            filename = sanitize_filename(image_info['title'] + get_extension(image_info['hdurl']))
            os.makedirs(path, exist_ok=True)
            get_image(filename, nasa_path, image_info['hdurl'])
            nasa_images_path.append(f"{nasa_path}/{filename}")
            number_of_pictures = number_of_pictures + 1
        else:
            errors = errors + 1
    print("images from Nasa:", number_of_pictures)
    print("  errors:", errors)
    return nasa_images_path


def get_extension(url):
    file_path = urlparse(url)
    extension = os.path.splitext(file_path.path)[1]
    return extension
