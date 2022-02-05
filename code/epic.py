import requests
from common import get_image

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