import logging
import os
import requests
from common import download_image
from pathvalidate import sanitize_filename
from urllib.parse import urlparse


def get_apod_images(nasa_api_key, apod_path="../apod_photos"):
    params = {
        "count": 30,
        "api_key": nasa_api_key}
    number_of_pictures = 0
    errors = 0
    apod_url = f"https://api.nasa.gov/planetary/apod"
    apod_images_path = []
    response = requests.get(apod_url, params)
    response.raise_for_status()
    images_info = response.json()
    os.makedirs(apod_path, exist_ok=True)
    for image_info in images_info:
        if 'hdurl' in image_info:
            filename = sanitize_filename(image_info['title'] + get_extension(image_info['hdurl']))
            download_image(filename, apod_path, image_info['hdurl'])
            apod_images_path.append(f"{apod_path}/{filename}")
            number_of_pictures = number_of_pictures + 1
        else:
            errors = errors + 1
    logging.info(f"images from Astronomy Picture of the Day: {number_of_pictures}")
    logging.warning(f"errors: {errors}")
    return apod_images_path


def get_extension(url):
    file_path = urlparse(url)
    extension = os.path.splitext(file_path.path)[1]
    return extension
