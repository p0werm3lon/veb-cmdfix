from urllib.parse import urlparse
from random import choice
from string import ascii_letters

from editor import editor

import requests
import os

def getExt(url):
    _, extension = os.path.splitext(url)
    return extension

def makeDest():
    return ''.join(choice(ascii_letters) for i in range(10))

def download(url):
    resp = requests.get(url)
    dest = f'./tmp/{makeDest()}{getExt(url)}'

    if resp.status_code==200:
        with open(dest, 'wb') as file:
            file.write(resp.content)
            return dest
    else:
        print("Couldn't download file")

# file = download("https://cdn.discordapp.com/attachments/1070877058823102584/1139679874290831461/IMG_0132.jpg")
# print(file)
# try:
#     result = editor(file, "e=1") # result.filename
# except Exception as e:
#     print(e)