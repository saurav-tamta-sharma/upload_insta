import os
from instagrapi import Client
from instagrapi.types import Usertag, Location

imgdir = "D:\\pythonProject\\images\\"  # add directory of folder


def listDir(dir):
    filename = (os.listdir(dir)[0])
    global a
    a = os.path.abspath(os.path.join(dir, filename))
    return a


if __name__ == '__main__':
    listDir(imgdir)

cl = Client()
cl.login(username="brimbiii", password="55sept")

media = cl.photo_upload(
    path=a,
    caption="random"     #for caption
)
