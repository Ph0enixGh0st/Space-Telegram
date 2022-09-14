import argparse
import os
import requests

from dotenv import load_dotenv
from importlib.resources import path
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import urlencode


def fetch_nasa_apod_images(path="tg_upload_photos_pool\\", count=5):
  
  load_dotenv()

  api_key = os.environ['NASA_API_KEY']

  Path(f"{path}").mkdir(parents=True, exist_ok=True)

  nasa_apod_url = "https://api.nasa.gov/planetary/apod?"
  encoded_url = nasa_apod_url + urlencode({'api_key': api_key, 'count': f'{count}'})
  response = requests.get(encoded_url)
  response = response.json()

  n = 0
  
  for photo in response:
    file_name = "nasa_" + str(n)
    url = response[n]["url"]
    nasa_photo = requests.get(url)
    with open(f"{path}/{file_name}.jpeg", 'wb') as file:
        file.write(nasa_photo.content)
    n += 1
    print(f"Here goes APOD photo #{n}")


def main():
  
  load_dotenv()
  
  parser = argparse.ArgumentParser(
  description='The script downloads photos from NASA APOD API'
  )
  parser.add_argument("-q", "--qty", help='Enter the photos quantity you want (5 pcs by default).', type=int)
  args = parser.parse_args()
  if args.qty is not None:
    count = int(args.qty)
  else:
    count = 5
  
  fetch_nasa_apod_images("tg_upload_photos_pool\\", count)
  print("Task completed")


if __name__ == '__main__':
    main()
