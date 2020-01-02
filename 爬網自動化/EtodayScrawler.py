#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import os
import pandas as pd
import time
import json
import re
import pymongo
from hdfs import *
client = Client("http://namenode:9870",root="/",timeout=100,session=False)
try:
    with client.read('/user/hdfs/news/ENsignal.txt', encoding='utf-8') as reader:
        singal =reader.read()
    client.delete('/user/hdfs/news/ENsignal.txt')
except:
    singal='2020年信用卡優惠縮水　一次讓你搞懂哪些好康被吃掉'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
url ='https://www.ettoday.net/news_search/doSearch.php?keywords=%E4%BF%A1%E7%94%A8%E5%8D%A1&idx=2&page=1'
df = pd.DataFrame(columns=['標題', '時間', '網址', '內文'])

index = 0
page=2
k=0
while True:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    Enter_url = soup.select('h2 a ')
    try:
        for i in Enter_url:
            url01 = i['href']
            title01 = i.text

            print(url01)
            print(title01)
            if index == 0:
                Nsignal = title01
            if title01 == singal or index >100:
                break
            res01 = requests.get(url01, headers=headers)
            soup01 = BeautifulSoup(res01.text, 'html.parser')
            article = soup01.select('div[class="story"] p')
            time = soup01.select('time')[0].text
            time = time.strip()
            print(time)
            j = ''
            for i in article:
                j += i.text + '\n'
            # print(j)

            df.loc[index] = title01, time, url01, j
            index += 1
    except Exception as e:
        print('erro:', e + str(len(df)))

    print(len(df))

    if k == len(df):
        break
    k = len(df)

    url = "https://www.ettoday.net/news_search/doSearch.php?keywords=%E4%BF%A1%E7%94%A8%E5%8D%A1&idx=2&page=" + str(
        page)
    page += 1
    if title01 == singal or index >100:
        break
if index >0:
    if 'Etoday.csv' in client.list("/user/hdfs/news/"):
        with client.write('/user/hdfs/news/Etoday.csv', append=True, encoding='utf-8') as writer:
            df.to_csv(writer)
    else:
        with client.write('/user/hdfs/news/Etoday.csv', encoding='utf-8', overwrite=True) as writer:
            df.to_csv(writer)
with client.write('/user/hdfs/news/ENsignal.txt', encoding='utf-8') as writer:
    writer.write(Nsignal)
print(df)
print(Nsignal)
