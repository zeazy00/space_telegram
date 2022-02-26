import requests
from common import get_image

number_of_pictures = 0


def fetch_spacex_last_launch(spacex_path):
    spacex_url = "https://api.spacexdata.com/v4/launches/latest"
    spacex_images_path = []
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    if not links:
        print("no spasex links")
    else:
        for file_number, link in enumerate(links,  start=1):
            filename = f"spacex{file_number}.jpg"
            os.makedirs(path, exist_ok=True)
            get_image(filename, spacex_path, link[1])
            spacex_images_path.append(f"{spacex_path}/{filename}")
            number_of_pictures = number_of_pictures + 1
        print("images from SpaceX:", number_of_pictures)
    return spacex_images_path
