import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import re
import os
import pandas as pd
import time
import xlsxwriter

driver=Chrome('./chromedriver')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

url='https://www.pixnet.net/tags/%E4%BF%A1%E7%94%A8%E5%8D%A1'

df=pd.DataFrame(columns=['標題','時間','網址','內文'])
index=0

driver.get(url)
a=[]
b=0;k=0
while True:
    for i in range(1000):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight-document.body.scrollHeight*0.2)")
        time.sleep(1)

        a=driver.find_elements_by_css_selector("a")
        print(len(a))

        if len(a)==k:
            b=b+1
            print('b:',b)
            if b>15:
                break
        else:
            b=0
        k = len(a)
    k=len(a)
    if k>8000:
        k=0
        b=0
        break

c=0
for i in a:
    try:
        i=i.get_attribute('href')
        l=re.findall(r'[h].*/[b].*[g]/[p].*',i)
        if l != []:
            url_in=str(l[0])
            a=re.findall(r'\d\d\d\d\d\d\d\d\d',url_in)
            if a!=[]:
                aa=int(a[0])
                print(aa)

                if c!=aa:
                    c=aa
                    print(url_in)
                    res = requests.get(url_in, headers=headers)
                    res.encoding = 'utf-8'
                    soup = BeautifulSoup(res.text, 'html.parser')
                    airticle = soup.select('div[class="article-content"]')
                    tittle = soup.select('h2 a')
                    time= soup.select('li span')
                    if len(url_in)>100:
                        url_in=url_in[:100]

                    for ii,airticle_c in enumerate(airticle) :
                        tittle=tittle[ii].text
                        print(tittle)
                        time01=''
                        for t in time:
                            time01+=str(t.text)

                        airticle_c=str(airticle_c.text)
                        g=re.sub(r'//.*>','',airticle_c)
                        g = re.sub(r'//.*\[', '', g)
                        g = re.sub(r'\(a.*;', '', g)
                        g=g.split('(function()')[0]
                        g = re.sub(r'\w.*;', '', g)
                        g = re.sub(r'\(.*{', '', g)
                        g = re.sub(r'}.*', '', g)
                        g = re.sub(r'\w*.*\(.*', '', g)
                        g = re.sub(r'\n\n\n', '', g)
                        print(g)

                        df.loc[index] = tittle, time01, url_in, g
                        index += 1
    #
    except :
        print('g')
print(df)
df.to_json('ppk.json',orient='index',force_ascii=False)
df.to_csv('ppk.csv',encoding='utf-8')
df.to_excel('ppk.xlsx')


# res=requests.get(url, headers=headers)
# res.encoding='utf-8'
# soup=BeautifulSoup(res.text,'html.parser')
# t1=soup.select('div[class="information"]')
# print(t1)
# for i in range(1, 40):
#     driver.execute_script('document.documentElement.scrollTop = document.documentElement.scrollHeight;')
#     time.sleep(5)