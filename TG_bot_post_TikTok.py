# -*- coding: utf-8 -*-

from TikTokApi import TikTokApi

import youtube_dl
import telebot
import re, os, sys, time
import random
import requests
import urllib
from tqdm import tqdm
from urllib import request
from urllib.parse import quote

TOKEN = "" #Токен бота
CHAT_ID = "@" # @chanel

dir = "/home/user/"  #Путь сохранения видео

to_wait = 1 #Перерыв между сообщениями в минутах

#hash_tag = "тренды"

api = TikTokApi()

mylist = [1,2,3,4,5,6,7,8,9,10]

wait = to_wait * 60

count = 1

while True:

    tiktoks = api.byHashtag("тренды", count=count, language='en', proxy="https://51.161.116.223:3128")

    for tiktok in tiktoks:
        t_video = tiktok['id']
        t_chanel = tiktok['author']['uniqueId']

    tiktokData = api.get_Video_By_DownloadURL("https://www.tiktok.com/" + t_chanel + "/video/" + t_video, return_bytes=1)

    tiktokData = api.get_Video_By_TikTok(api.trending(count=1)[0])

    with open("v_tik.mp4", "wb") as out:
        out.write(tiktokData)

    print(u"Видео скачано")

    bot = telebot.TeleBot(TOKEN)

    print(u"Видео отправляется на канал")

    url = "https://api.telegram.org/bot" + TOKEN + "/sendVideo";
    files = {'video': open('v_tik.mp4', 'rb')}
    data = {'chat_id' : CHAT_ID}

    for i in tqdm(mylist): #Загрузка видео на канал визуально
        r = requests.post(url, files=files, data=data)

    files = "" #Костыль, его не трогать!

    print(u"Видео отправленно")

    os.system("rm v_tik.mp4")

    print(u"Видео удаленно")

    time.sleep(wait)

    os.system("clear")
