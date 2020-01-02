#!/usr/bin python
# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import json
import os, time, re
import pandas as pd
import time
import pandas as pd
import re
import pymongo
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/creditcard/index.html'
index=0
df = pd.DataFrame(columns=['標題', '時間', '網址', '內文'])
client = pymongo.MongoClient(host='123.241.175.34', port=27017)

#mongodb帳號密碼

client.admin.authenticate('root', '1qaz@WSX3edc')

#設定名稱為test的資料庫 也可用 db = client['test']

db = client.Recommend_card

#設定名稱為creditcard的collection  也可用coll = db['creditcard']

coll = db.ptt
try:
    mondata = coll.find_one({'mark':'ptts'})
    signal=mondata['signal']
    coll.delete_one({'mark':'ptts'})
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
    data = json.loads(df.T.to_json()).values()
    #將資料存入mongodb
    coll.insert_many(data)
coll.insert_one({"signal":Nsignal,'mark':'ptts'})
print(df)
print(Nsignal)
