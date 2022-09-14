import argparse
import os
import random
import requests
import telegram
import time

from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import urlencode

import fetch_nasa_apod_images
import fetch_nasa_epic_images
import fetch_spacex_images


def tg_spam():
    
    load_dotenv()

    loop_on = True
    files_pool = []

    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    photo_path = "tg_upload_photos_pool\\"
        
    for root, dirs, files in os.walk(photo_path):
        files_pool = files
        #print(files_pool)
      
    while loop_on:

        for photo in files_pool:

            bot.send_message(chat_id="@SPP_Bot_dvmn_edu", text=f"uploaded {photo}")
            bot.send_document(chat_id="@SPP_Bot_dvmn_edu", document=open(f'{photo_path}\\{photo}', 'rb'))
            time.sleep(float(os.environ.get('LOG_INTERVAL')))

        random.shuffle(files_pool)


def main():
  
    load_dotenv()

    fetch_nasa_apod_images.main()
    fetch_nasa_epic_images.main()
    fetch_spacex_images.main()

    tg_spam()


if __name__ == '__main__':
    main()