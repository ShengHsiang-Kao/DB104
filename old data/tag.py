import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import re
import os
import pandas as pd
import time
import xlsxwriter
import jieba

bank={'中信':'中信','中國信託':'中信' ,'玉山':'玉山','Richart':'Richart', 'richart':'Richart','KOKO':'KOKO','koko':'KOKO',
       '國泰':'國泰','國泰世華':'國泰','台新':'台新','永豐':'永豐','兆豐':'兆豐'}

card={'linepay':'Linepay','Linepay':'Linepay','LinePay':'Linepay','LINEPAY':'Linepay','GOGO':'GOGO','gogo':'GOGO',
       'flygo':'Flygo','Flygo':'Flygo','FLYGO':'Flygo','大戶':'dawho','dawho':'dawho','Dawho':'dawho',
       'PI':'Pi','Pi':'Pi','pi卡':'Pi','PI卡':'Pi','ubear':'Ubear','UBEAR':'Ubear','Ubear':'Ubear','ubear':'Ubear',
      'only':'Only','ONLY':'Only','Only':'Only'}

behavior={'跑步':'運動','健身房':'運動','運動':'運動','旅遊':'旅遊','旅行':'旅遊','機票':'旅遊','飯店':'旅遊','機場':'旅遊','旅平險':'旅遊','出國':'旅遊','保險':'保險','保費':'保險',
         '加油':'加油','中油':'加油','國外':'國外','海外':'國外','電影':'電影','國賓':'電影','威秀':'電影'}

jieba.load_userdict(r'C:/Users/Big data/PycharmProjects/ourETL/userdict.txt')
df=pd.read_json(r'C:/Users/Big data/PycharmProjects/ourETL/Reene.json')
# print(df)
# print(len(df.loc['斷詞']))

bank_l=[]
for ii in range(len(df.loc['斷詞'])):
    cont=df.loc['斷詞'][ii]
#   print(ii)
    b_tag={}
    for i in cont:
        if i in bank:
            if i not in b_tag:
                b_tag[i]=1
            else:
                b_tag[i]+=1
    bank_l.append(b_tag)
print(bank_l)


card_l=[]
for ii in range(len(df.loc['斷詞'])):
    cont=df.loc['斷詞'][ii]
#   print(ii)
    c_tag={}
    for i in cont:
        if i in card:
            if i not in c_tag:
                c_tag[i]=1
            else:
                c_tag[i]+=1
    card_l.append(c_tag)
print(card_l)


act_l=[]
for ii in range(len(df.loc['斷詞'])):
    cont=df.loc['斷詞'][ii]
#   print(ii)
    act_tag={}
    for i in cont:
        if i in behavior:
            if i not in act_tag:
                act_tag[i]=1
            else:
                act_tag[i]+=1
    act_l.append(act_tag)
print(act_l)