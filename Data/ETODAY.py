import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import re
import os
import pandas as pd
import time
import xlsxwriter



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
            url01=i['href']
            title01=i.text
            print(url01)
            print(title01)
            res01 = requests.get(url01, headers=headers)
            soup01 = BeautifulSoup(res01.text, 'html.parser')
            article = soup01.select('div[class="story"] p')
            time = soup01.select('time')[0].text
            time=time.strip()
            print(time)
            j=''
            for i in article:
                j+=i.text+'\n'
            # print(j)
            df.loc[index] = title01, time, url01, j
            index += 1
    except:
        print('erro:'+str(len(df)))

    print(len(df))

    if k==len(df):
        break
    k=len(df)
    url="https://www.ettoday.net/news_search/doSearch.php?keywords=%E4%BF%A1%E7%94%A8%E5%8D%A1&idx=2&page="+str(page)
    page+=1


df.to_json('Etoday.json',orient='index',force_ascii=False)
df.to_csv('Etoday.csv',encoding='utf-8')
df.to_excel('Etoday.xlsx')
