#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re
import pymongo
from hdfs import *
client = Client("http://namenode:9870",root="/",timeout=100,session=False)

useragent= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers={'User-Agent':useragent}


try:
    with client.read('/user/hdfs/news/UdnNsignal.txt', encoding='utf-8') as reader:
        signal =reader.read()
    client.delete('/user/hdfs/news/UdnNsignal.txt')
except:
    signal='春節瘋旅日？北富銀J卡三周大増20萬張 搶卡王寶座' #如果沒有存過就爬到這裡

title01=''
n=1
index=0
df=pd.DataFrame(columns=['標題','發布時間','網址','內文'])
while True:
    url = f'https://udn.com/search/tagging/2/%E4%BF%A1%E7%94%A8%E5%8D%A1/{n}'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('div[id="search_content"]')
    html = soup.select('div[id="search_content"]')[0].select('dt')
    # print(html)
    for i in html:
        title = i.h2.text
        if index == 0:
            Nsignal = title
        if title == signal or index >100:
            break
        #print(title)
        date = re.findall(r'\d\d\d\d-\d\d-\d\d', i.span.text)
        #         print(date[0])
        t_url = i.a['href']
        #         print(t_url)
        try:
            url_a = i.a['href']
            res_a = requests.get(url_a, headers=headers)
            soup_a = BeautifulSoup(res_a.text, 'html.parser')
            content = soup_a.select('div[id="story_body_content"]')[0].select('p')
            article = ''.join(a.text for a in content)  # 內文
        except:
            pass

        if title !=title01:
            df.loc[index] = title, date[0], url_a, article
            index += 1
            title01=title
    #         print('-----------------------------')

    if title == signal or index >100:
        break
    n += 1


if index >0:
    if 'udn.csv' in client.list("/user/hdfs/news/"):
        with client.write('/user/hdfs/news/udn.csv', append=True, encoding='utf-8') as writer:
            df.to_csv(writer)
    else:
        with client.write('/user/hdfs/news/udn.csv', encoding='utf-8', overwrite=True) as writer:
            df.to_csv(writer)
with client.write('/user/hdfs/news/UdnNsignal.txt', encoding='utf-8') as writer:
    writer.write(Nsignal)
print(df)
print(Nsignal)
