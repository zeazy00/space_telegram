import os
import requests

def get_image(filename, path, url):
	os.makedirs(path, exist_ok=True)

	response = requests.get(url)
	response.raise_for_status()

	file_path = f"{path}/{filename}"

	with open(file_path, 'wb') as file:
		file.write(response.content)