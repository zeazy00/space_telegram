import requests
from common import get_image

def fetch_spacex_last_launch(spacex_path):
	spacex_url = "https://api.spacexdata.com/v4/launches/latest"
	spacex_images_path = []
	response = requests.get(spacex_url)
	response.raise_for_status()
	links = response.json()["links"]["flickr"]["original"]
	if not links:
		print("no spasex links")
	else:
		for link in enumerate(links):
			filename = f"spacex{link[0]+1}.jpg"
			print("1)", spacex_path, "2)", filename, "3)", link[1])
			get_image(filename, spacex_path, link[1])
			spacex_images_path.append(f"{spacex_path}/{filename}")
	return spacex_images_path