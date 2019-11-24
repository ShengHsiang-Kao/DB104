# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
from my_fake_useragent import UserAgent
import os, time, re
import pandas as pd
from selenium.webdriver import Chrome
import openpyxl

def random_header():
    ua = UserAgent()
    random_header = json.loads(r'''{
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.dogforum.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent":"%s"
    }'''%ua.random)
    return random_header
########################################################
# resource_path = r'./DCard'
# if not os.path.exists(resource_path):
#     os.mkdir(resource_path)

headers = {'User-Agent':str(random_header())}

driver = Chrome('./chromedriver')
driver.implicitly_wait(3)
url = 'https://www.dcard.tw/f/creditcard/'
driver.get(url)

for i in range(1, 100):
    driver.execute_script('document.documentElement.scrollTop = document.documentElement.scrollHeight;')
    time.sleep(5)

soup = BeautifulSoup(driver.page_source, features="html.parser")
nalr = soup.select('div[class="PostList_entry_1rq5Lf"] a[class="PostEntry_root_V6g0rd"]')

index = 0
k= pd.DataFrame(columns=['編號','標題','時間','網址','內文'])

for j in nalr:
    # print(j)
    title_url = 'https://www.dcard.tw' + j['href']
    # print(title_url)
    req2 = requests.get(title_url, headers=headers)
    soup2 = BeautifulSoup(req2.text, 'html.parser')
    content = soup2.select('div.Post_content_NKEl9d div')
    title = soup2.select('h1[class="Post_title_2O-1el"]')
    print(title)
    for t in title:
        article_text=''
        for each_content, n in enumerate(content):
            article_title = t.text            
            if each_content%3==2:
#                 print(n.text)
                article_text += n.text+('\n')
        print(article_text)
        print()
        time = soup2.select('span[class="Post_date_2ipeYS"]')
        article_time = ''
        for m in time:
            article_time += m.text
#             print(article_time)
#         try:
#             with open(r'./Dtest/%s.txt'%(t.text), 'a', encoding='utf-8') as f:
#                 f.write(n.text+'\n')
#         except:
#             with open(r'./Dtest/article%s.txt' % (len(n)), 'a', encoding='utf-8') as f:
#                 f.write(n.text+'\n')
    k.loc[index]= index,article_title,article_time,title_url,article_text
    print(index)
    index += 1

k


#把全形字或標點符號轉成半形, 轉成半形之後的標點符號才可被isalpha()清掉
def conv_wide(text):
    code = ord(str(text))
    if x == u'\u3000': #space
        code = 32
    elif u'\uff01' <= text <= u'\uff5e':
        code -= 65248
    return chr(code)



import jieba
jieba.load_userdict(r'./userdict.txt')
content=k['內文']
cut_list=[]
wordc_list=[]
for j in range(len(content)):
    cut_content=jieba.lcut(content[j])
    cut_list.append(cut_content)
    word_count={}
    for word in cut_content:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    wordc_list.append(word_count)
k['斷詞']=cut_list
k['詞頻']=wordc_list

print(len(k['內文']))
print(len(cut_list))
print(len(wordc_list))

# +
# os.getcwd()
# -

#csv file but opened with excel will be garbled text
k.to_csv(r'./dcard_creditcard.csv', index=0, encoding='utf-8')

k.to_json(r'./dcard_creditcard.json', orient='index', force_ascii=False)

#need to import openpyxl
import openpyxl
k.to_excel("dcard.xlsx")

#can be opened with excel
k.to_csv(r'./dcard_creditcard.csv', index=0, encoding='utf-16')

title=k['標題']
title_index=[]
for num, i in enumerate(title):
    review=re.findall(r'.*心得.*',i)
    if review !=[]:
        title_index.append(num)
    review=re.findall(r'.*核卡.*',i)
    if review !=[]:
        if num not in title_index:
            title_index.append(num)
print(title_index)
for ind in title_index:
    print(k['標題'][ind])
# print(len(title_index))

#synonym dictionary
synonym_dict={}
synonym_path=r'./synonym.txt'
with open(synonym_path,'r',encoding='utf-8') as syn:
    syn_str=syn.read().split('\n')
for each_row in syn_str:
    synonum_dict[each_row.split(',')[0]]=[item for item in each_row.split(',')] 

synonum_list=[]
for i in syn_str:
    each_word=i.split(',')
    synonum_list += each_word
# print(synonum_list)
for word_tmp in k['斷詞']:
    for num, i in enumerate(word_tmp):
        for key in synonum_dict:
            for word_value in synonum_dict[key]:
                if i == word_value:
                    word_tmp[num] = key
# print(k['斷詞'][317])
# re-join to article after replacing synonum
for i in range(len(k['斷詞'])):
    k['內文'][i]=''.join(k['斷詞'][i])
print(k['內文'][869])

df_2= pd.DataFrame(columns=['編號','內文','斷詞','申請卡別','職業','年資','年齡','已持有','貸款','額度','近三個月申請','年收入','財力證明'])
for num, i in enumerate(title_index):
    con=k['內文'][i]
    cut=k['斷詞'][i]
    card=re.findall(r'(.*申辦.*)\n',con)
    job=re.findall(r'(.*職業.*)\n',con)
    year=re.findall(r'(.*年資.*)\n',con)
    age=re.findall(r'(.*年齡.*)\n',con)
    have=re.findall(r'(.*已持有.*)\n',con)
    debit=re.findall(r'(.*貸款.*)\n',con)
    limit=re.findall(r'(.*額度.*)\n',con)
    sal=re.findall(r'(.*年收.*)\n',con)
    proof=re.findall(r'(.*財力證明.*)\n',con)
    df_2.loc[num]= i,con,cut,card,job,year,age,have,debit,limit,'0',sal,proof

df_2

df_2.to_json(r'./dcard_synonym.json', orient='index', force_ascii=False)

import xlsxwriter
writer = pd.ExcelWriter('dcard_synonym.xlsx', engine='xlsxwriter')
df_2.to_excel(writer, sheet_name='Sheet1')
writer.save()

import pandas as pd
import json
df_3=pd.read_json(r'./dcard_creditcard_cut.json')
df_3

bank={'中信':'中信','中國信託':'中信' ,'玉山':'玉山','Richart':'Richart', 'richart':'Richart','KOKO':'KOKO','koko':'KOKO',
       '國泰':'國泰','國泰世華':'國泰','台新':'台新','永豐':'永豐','兆豐':'兆豐'}
card={'linepay':'Linepay','Linepay':'Linepay','LinePay':'Linepay','LINEPAY':'Linepay','GOGO':'GOGO','gogo':'GOGO',
       'flygo':'Flygo','Flygo':'Flygo','FLYGO':'Flygo','大戶':'dawho','dawho':'dawho','Dawho':'dawho',
       'PI':'Pi','Pi':'Pi','pi卡':'Pi','PI卡':'Pi','ubear':'Ubear','UBEAR':'Ubear','Ubear':'Ubear','ubear':'Ubear',
      'only':'Only','ONLY':'Only','Only':'Only'}
behavior={'跑步':'運動','健身房':'運動','運動':'運動','旅遊':'旅遊','旅行':'旅遊','機票':'旅遊','飯店':'旅遊','機場':'旅遊','旅平險':'旅遊','出國':'旅遊','保險':'保險','保費':'保險',
         '加油':'加油','中油':'加油','國外':'國外','海外':'國外','電影':'電影','國賓':'電影','威秀':'電影'}

df_3
df_3['銀行']=None
df_3['卡片']=None
df_3['行為']=None

for article in range(len(df_3)):
    article_bank={}
    for word in df_3['斷詞'][article]:
        if word in bank:
            if bank[word] not in article_bank:
                article_bank[bank[word]] = 1
            else:
                article_bank[bank[word]] += 1
    print(article_bank)
    df_3['銀行'][article]=article_bank   

for article in range(len(df_3)):
    article_card={}
    for word in df_3['斷詞'][article]:
        if word in card:
            if card[word] not in article_card:
                article_card[card[word]] = 1
            else:
                article_card[card[word]] += 1
    print(article_card)
    df_3['卡片'][article]=article_card   

for article in range(len(df_3)):
    article_behavior={}
    for word in df_3['斷詞'][article]:
        if word in behavior:
            if behavior[word] not in article_behavior:
                article_behavior[behavior[word]] = 1
            else:
                article_behavior[behavior[word]] += 1
    print(article_behavior)
    df_3['行為'][article]=article_behavior   

df_3

df_3.to_json(r'./dcard_tag.json', orient='index', force_ascii=False)

import xlsxwriter
writer = pd.ExcelWriter('dcard_tag.xlsx', engine='xlsxwriter')
df_3.to_excel(writer, sheet_name='Sheet1')
writer.save()
