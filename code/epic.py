import requests
from common import get_image

number_of_pictures = 0


def get_epic_images(epic_path, nasa_api_key):
    last_date_epic_url = f"https://api.nasa.gov/EPIC/api/natural?api_key={nasa_api_key}"
    epic_images_path = []
    response = requests.get(last_date_epic_url)
    response.raise_for_status()
    images_info = response.json()
    for image_info in images_info:
        photo_date = image_info["date"].replace("-", "/").split()[0]
        filename = f'{image_info["image"]}.png'
        epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{filename}?api_key={nasa_api_key}'
        os.makedirs(path, exist_ok=True)
        get_image(filename, epic_path, epic_photo_url)
        epic_images_path.append(f"{epic_path}/{filename}")
        number_of_pictures = number_of_pictures + 1
    print("images from EPIC:", number_of_pictures)
    return epic_images_path
