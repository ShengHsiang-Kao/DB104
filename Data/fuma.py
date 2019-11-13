import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import openpyxl

import time
# path='./artical'
# if not os.path.exists(path):
#     os.mkdir(path)

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
url = 'http://ewdna.com/search?q=信用卡'

df=pd.DataFrame(columns=['標題','時間','網址','內文'])
index=0

for i in range(70):
    res=requests.get(url, headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    Enter_url=soup.select('h3[class="post-title entry-title"] a')
    p_time=soup.select('a [class="published"]')

    for int,tite in enumerate(Enter_url):
        tittle=tite.text
        print(tittle)
        ptime=p_time[int].text
        # print(ptime)
        k=str(tite)
        url_t=re.findall(r'[h][t].*[l]',k)[0]
        # print(url_t)
        try:
            res_t = requests.get(url_t, headers=headers)
            soup_t = BeautifulSoup(res_t.text, 'html.parser')
            artical=soup_t.select('div[class="post-body entry-content float-container"]')[0].text
            # print(artical)
            df.loc[index]=tittle,ptime,url_t,artical
            index +=1

            # with open(r'%s/%s.txt' % (path, title), 'w', encoding='utf-8')as w:
            #     w.write(artical)
            #

        except:
            print('---------------------------------------------')

    next_U='http://ewdna.com/search?q=信用卡&max-results=20&start=%s'%(20*(i+1))
    url=next_U
    print(i)
print(df)
df.to_json('credix03.json',orient='index',force_ascii=False)
df.to_csv('credcsv03.csv',encoding='utf-8')
df.to_excel('credexcel03.xlsx')