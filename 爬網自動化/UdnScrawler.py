import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re
import pymongo

useragent= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
headers={'User-Agent':useragent}


client = pymongo.MongoClient(host='123.241.175.34', port=27017)
#mongodb帳號密碼
client.admin.authenticate('root', '1qaz@WSX3edc')
#設定名稱為test的資料庫 也可用 db = client['test']
db = client.Recommend_card
#設定名稱為creditcard的collection  也可用coll = db['creditcard']
coll = db.Udnews

try:
    mondata = coll.find_one({'mark':'udns'})  #上次爬的地方做記號
    signal=mondata['signal']
    coll.delete_one({'mark':'udns'})

except:
    signal='搶紅包年終財 永豐銀數位帳戶1.1%活存再延半年' #如果沒有存過就爬到這裡

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
        if title == signal:
            break
        print(title)
        date = re.findall(r'\d\d\d\d/\d\d/\d\d', i.span.text)
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

    if title == signal:
        break
    n += 1

if index >0:
    data = json.loads(df.T.to_json()).values()
    #將資料存入mongodb
    coll.insert_many(data)
coll.insert_one({"signal":Nsignal,'mark':'udns'})
print(df)
print(Nsignal)
