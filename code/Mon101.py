import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import re
import os
import pandas as pd
import time
import xlsxwriter

# driver=Chrome('./chromedriver')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
url = 'https://www.money101.com.tw/blog/category/credit-cards/creditcard-activities-promotions'
k=0
df = pd.DataFrame(columns=['標題', '時間', '網址', '內文'])
index = 0
for p in range(2,4):
# driver.get(url)
# a = driver.find_elements_by_css_selector("a")
# print(a)

    res=requests.get(url, headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    Enter_url=soup.select('h1 a ')
    for i in Enter_url:
        title = i.text
        print(title)
        url01=i ['href']
        print(url01)
        res01 = requests.get(url01, headers=headers)
        soup01 = BeautifulSoup(res01.text, 'html.parser')
        article = soup01.select('div[class="entry-content"] ')
        art=article[0].text
        art=re.split('立即訂閱',art)[0]
        print(art)
        # time01 = soup01.select('time')
        # time=time01[0].text
        # print(time)
        df.loc[index] = title, time, url01, art
        index += 1
#     print(p)
#     url='https://www.money101.com.tw/blog/category/credit-cards/creditcard-activities-promotions/page/%s'%(p)
#     if k==len(df):
#         break
#     k=len(df)
#
# print(df)
# df.to_json('credix05.json',orient='index',force_ascii=False)
# df.to_csv('credcsv05.csv',encoding='utf-8')
# df.to_excel('credexcel05.xlsx')