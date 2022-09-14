# Space-Telegram
The script downloads photos from NASA and SpaceX for further upload into Telegram channel.

## How to install
Using GitHub CLI:
```bash
gh repo clone Ph0enixGh0st/Space-Telegram
```

Or download and unpack ZIP file from GIT Hub repository: https://github.com/Ph0enixGh0st/Space-Telegram.git

# Prerequisites
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

# telegram_space_photo_spam.py
The script downloads photos from NASA and SpaceX API and then uploads them into Telegram channel via bot in infinite loop.

## How to run telegram_space_photo_spam.py
```bash
python telegram_space_photo_spam.py
```
![image](https://user-images.githubusercontent.com/108229516/190182368-05d7d0fb-928e-450c-85aa-da1a42c37209.png)


# fetch_nasa_apod_images.py
The script downloads images from NASA APOD API (Astronomy Picture of the Day). By default 5 images will be downloaded.

## How to run fetch_nasa_apod_images.py
```bash
python fetch_nasa_apod_images.py -q {qty}
```
![image](https://user-images.githubusercontent.com/108229516/190181486-fd3b49ff-949f-47fe-acc9-12f0b01dd482.png)

![image](https://user-images.githubusercontent.com/108229516/190181244-631069dc-59ab-4f44-923a-cd46b58fd8bb.png)


# fetch_nasa_epic_images.py
The script downloads images from NASA EPIC API (Earth Polychromatic Imaging Camera). By default 15 images will be downloaded.

## How to run fetch_nasa_epic_images.py
```bash
python fetch_nasa_epic_images.py -q {qty}
```
![image](https://user-images.githubusercontent.com/108229516/190183357-baa20446-ca03-4471-bec7-8ce590dba149.png)

![image](https://user-images.githubusercontent.com/108229516/190182910-b44c0333-ef85-4c73-8800-c34173b061db.png)


# fetch_spacex_images.py
The script downloads Space X launches images by launch id number. If launch id is not provided the script will download the latest launch photos.

## How to run fetch_spacex_images.py
```bash
python fetch_spacex_images.py -l {launch id}
```
![image](https://user-images.githubusercontent.com/108229516/190184756-c3f669c7-ade3-478d-be58-671da5a15aee.png)

![image](https://user-images.githubusercontent.com/108229516/190183896-175d7859-05f8-4b20-b810-764ce2449f13.png)


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
