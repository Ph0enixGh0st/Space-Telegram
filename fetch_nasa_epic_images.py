import argparse
import os
import requests

from dotenv import load_dotenv
from importlib.resources import path
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import urlencode


def get_nasa_epic(path="tg_upload_photos_pool\\", count=15):

  load_dotenv()

  api_key = os.environ['NASA_API_KEY']
  nasa_epic_all_photo_dates_url = "https://api.nasa.gov/EPIC/api/natural/all?"
  encoded_url = nasa_epic_all_photo_dates_url + urlencode({'api_key': api_key})
  all_dates_response = requests.get(encoded_url)
  all_dates_response = all_dates_response.json()
  
  cycle_count = 0
  
  for date in all_dates_response:

    while cycle_count < count:
            
      single_date = all_dates_response[cycle_count]["date"]
       
      url_blank = f"https://api.nasa.gov/EPIC/api/natural/date/{single_date}?"
      image_name_url = url_blank + urlencode({'api_key': api_key})

      image_name_response = requests.get(image_name_url)
      image_name_response = image_name_response.json()
      inr = image_name_response[0]["image"]
           
      single_date = single_date.replace("-", "/")
      
      nasa_epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{single_date}/png/{inr}.png?" + urlencode({'api_key': api_key})

      file_name = "nasa_epic_" + str(cycle_count)

      nasa_epic_photo = requests.get(nasa_epic_url)
      
      with open(f"{path}/{file_name}.png", 'wb') as file:
        file.write(nasa_epic_photo.content)
      
      cycle_count += 1
      
      print(f"Here goes EPIC photo #{cycle_count}")



def main():
    
  parser = argparse.ArgumentParser(
  description='The script downloads photos from NASA EPIC API'
  )
  # parser.add_argument("-p", "--path", help='Name the folder you want to save the photos to?')
  parser.add_argument("-q", "--qty", help='How many photos you want to download? Q-ty is 10 by default', type=int)
  args = parser.parse_args()
  # path = args.path
  if args.qty is not None:
    count = int(args.qty)
  else:
    count = 15
  
  path = "tg_upload_photos_pool\\"
  Path(f"{path}").mkdir(parents=True, exist_ok=True)

  get_nasa_epic(path, count)

  print("Task completed")

if __name__ == '__main__':
    main()