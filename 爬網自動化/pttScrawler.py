#!/usr/bin python
# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import json
import os, time, re
import pandas as pd
import time
import re
from hdfs import *

client = Client("http://namenode:9870",root="/",timeout=100,session=False)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/creditcard/index.html'
index=0
df = pd.DataFrame(columns=['標題', '時間', '網址', '內文'])



try:
    with client.read('/user/hdfs/news/Nsignal.txt', encoding='utf-8') as reader:
        signal =reader.read()
    client.delete('/user/hdfs/news/Nsignal.txt')
except:
    signal='Re: [情報] 6 Pay享6%，My樂94神'

while True:
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_title_html = soup.select('div[class="title"]')
    for each_article in article_title_html:
        try:
            titel01 = each_article.a.text
            if index == 0:
                Nsignal = titel01  # 第一筆會加進去做記號
            if titel01 == signal or index >100:  # 找到signal上次標題跳出
                break
            url01 = 'https://www.ptt.cc' + each_article.a['href']

            article_url = 'https://www.ptt.cc' + each_article.a['href']
            article_text = each_article.a.text
            article_res = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            article_content = article_soup.select('div#main-content')[0].text.split('--')[0]
            j = article_content
            time = re.findall(r'時間(.*)\n', article_content)[0]

            df.loc[index] = titel01, time, url01, j
            index += 1
        except:
            pass
    if titel01 == signal or index >100:  # 終止迴圈
        break
    url = 'https://www.ptt.cc' + soup.select('div[class="btn-group btn-group-paging"]')[0].select('a')[1]['href']

if index >0:
    if 'ptt.csv' in client.list("/user/hdfs/news/"):
        with client.write('/user/hdfs/news/ptt.csv', append=True, encoding='utf-8') as writer:
            df.to_csv(writer)

    else:
        with client.write('/user/hdfs/news/ptt.csv', encoding='utf-8', overwrite=True) as writer:
            df.to_csv(writer)

with client.write('/user/hdfs/news/Nsignal.txt', encoding='utf-8') as writer:
    writer.write(Nsignal)
print(df)
print(Nsignal)
