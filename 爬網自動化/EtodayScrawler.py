import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import os
import pandas as pd
import time
import json
import re
import pymongo

#連接 mongodb

client = pymongo.MongoClient(host='123.241.175.34', port=27017)

#mongodb帳號密碼

client.admin.authenticate('root', '1qaz@WSX3edc')

#設定名稱為test的資料庫 也可用 db = client['test']

db = client.Recommend_card

#設定名稱為creditcard的collection  也可用coll = db['creditcard']

coll = db.news

try:
    mondata = coll.find_one({'mark':'news'})
    singal=mondata['signal']
    coll.delete_one({'mark':'news'})
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
            if title01 == singal:
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
    if title01 == singal:
        break
if index >0:
    data = json.loads(df.T.to_json()).values()

#將資料存入mongodb

    coll.insert_many(data)
coll.insert_one({"signal":Nsignal,'mark':'news'})


print(df)
print(Nsignal)