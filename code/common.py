import os
import requests


def download_image(filename, path, url, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()

    file_path = f"{path}/{filename}"

    with open(file_path, 'wb') as file:
        file.write(response.content)
