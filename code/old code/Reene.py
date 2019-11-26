import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import xlsxwriter
from openpyxl import *
# path='./artical2'
# if not os.path.exists(path):
#     os.mkdir(path)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
url = 'https://ccwrenee.pixnet.net/blog'
df=pd.DataFrame(columns=['標題','時間','網址','內文'])
index=0
for iii in range(1):
    res = requests.get(url, headers=headers)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    Enter_url = soup.select('h2 a')
    # Enter_url = soup.select('ul[class="article-head"] h2 a')
    for j in Enter_url[0:3]:
        title=j.text
        print(j.text)
        url_i = j['href']
        print(url_i)
        res = requests.get(url_i, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        arti = soup.select('div[class="article"]')
        tt = soup.select('li[class="publish"]')[0].text
        print(tt)
        for k in arti :
            i=k.text.split('var deviceType')[0]
            i = re.sub(' ','', i)
            i = re.sub('\n\n', '\n', i)
            i = re.sub('\n\n\n', '\n', i)
            print(i)

            df.loc[index]=title,tt,url_i,i
            index +=1
            # try:
            #     with open(r'%s/%s.txt' % (path, title), 'w', encoding='utf-8')as w:
            #         w.write(i)
            # except:
            #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # url=r'https://ccwrenee.pixnet.net/blog'+str(iii)
# print(df)
# df.to_json('credix02.json',orient='index',force_ascii=False)
# df.to_csv('credcsv02.csv',encoding='utf-8')
# df.to_excel('credexcel02.xlsx')
# #
