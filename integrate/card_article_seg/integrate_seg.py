import pandas as pd
import json
import re
import pymongo
import jieba
import operator

#連接 mongodb
client = pymongo.MongoClient(host='123.241.175.34', port=27017)
#mongodb帳號密碼
client.admin.authenticate('root', '1qaz@WSX3edc')
#設定名稱為test的資料庫 也可用 db = client['test']
db = client.raw_article
#顯示db中所有collections
db.list_collection_names()
['article_social', 'article_web', 'article_news']
#drop collection
#db.article_socialjson.drop()
article_social=db.article_social.find()
article_web=db.article_web.find()
article_news=db.article_news.find()
df_article_social=pd.DataFrame(list(article_social))
df_article_web=pd.DataFrame(list(article_web))
df_article_news=pd.DataFrame(list(article_news))
df_article_web['seg']=None
#df_article_web['word_freq']=None
#df_article_web
n=len(df_article_web)
alltext=[]
stopset=set()
stop2=['/n','','\n']
with open(r'E:/專題/credit_card/DB104_hau/stop.txt','r',encoding='utf-8') as s:
    for line in s:
        stopset.add(line.strip('\n'))
jieba.load_userdict(r'E:/專題/credit_card/DB104_hau/userdict.txt')
for i in range(n):
    seg=[]
    wf={}
    text= str(df_article_web.loc[i]['content'])
    cut=jieba.lcut(text,cut_all=False)
    for j in cut:
        if j not in stopset:
            seg.append(cut)
    df_article_web['seg'][i]=seg
#     for w in seg.split(' '):
#         if w not in wf:
#             wf[w]=1
#         else:
#             wf[w]+=1
    #word_list=[wf.items() for k in wf if k not in stop2 ]
#     word_list=sorted(wf.items(),key=lambda a :a[1],reverse=True)
#     df_article_web['word_freq'][i]=word_list
del df_article_web['_id']
del df_article_web['content']
df_article_web[:3]
#article_social
df_article_social[:1]
df_article_social['seg']=None
#df_article_social['word_freq']=None
n=len(df_article_social)
alltext=[]
stopset=set()
stop2=['/n','','\n']
with open(r'E:/專題/credit_card/DB104_hau/stop.txt','r',encoding='utf-8') as s:
    for line in s:
        stopset.add(line.strip('\n'))
jieba.load_userdict(r'E:/專題/credit_card/DB104_hau/userdict.txt')
for i in range(n):
    seg=[]
    wf={}
    text= str(df_article_social.loc[i]['content'])
    cut=jieba.lcut(text,cut_all=False)
    for j in cut:
        if j not in stopset:
            seg.append(cut)
    df_article_social['seg'][i]=seg
#     for w in seg.split(' '):
#         if w not in wf:
#             wf[w]=1
#         else:
#             wf[w]+=1
#     #word_list=[wf.items() for k in wf if k not in stop2 ]
#     word_list=sorted(wf.items(),key=lambda a :a[1],reverse=True)
#     df_article_social['word_freq'][i]=word_list
del df_article_social['_id']
del df_article_social['content']


#df_article_news
df_article_news[:1]
df_article_news['seg']=None
#df_article_news['word_freq']=None
n=len(df_article_news)
alltext=[]
stopset=set()
stop2=['/n','','\n']
with open(r'E:/專題/credit_card/DB104_hau/stop.txt','r',encoding='utf-8') as s:
    for line in s:
        stopset.add(line.strip('\n'))
jieba.load_userdict(r'E:/專題/credit_card/DB104_hau/userdict.txt')
for i in range(n):
    seg=[]
    wf={}
    text= str(df_article_news.loc[i]['content'])
    cut=jieba.lcut(text,cut_all=False)
    for j in cut:
        if j not in stopset:
            seg.append(cut)
    df_article_news['seg'][i]=seg
#     for w in seg.split(' '):
#         if w not in wf:
#             wf[w]=1
#         else:
#             wf[w]+=1
#     #word_list=[wf.items() for k in wf if k not in stop2 ]
#     word_list=sorted(wf.items(),key=lambda a :a[1],reverse=True)
#     df_article_news['word_freq'][i]=word_list
del df_article_news['_id']
del df_article_news['content']

db_ETL = client.ETL
#collsoc = db.article_social
collweb = db_ETL.article_web_seg
collnews =db_ETL.article_news_seg
collsocial = db_ETL.article_social_seg
#將dataframe轉成能存入mongodb的json格式
data_social = json.loads(df_article_social.T.to_json()).values()
data_social[:2]
data_news = json.loads(df_article_news.T.to_json()).values()
data_web = json.loads(df_article_web.T.to_json()).values()
type(data_web)
#將資料存入mongodb
collsocial.insert_many(data_social)
collnews.insert_many(data_news)
collweb.insert_many(data_web)
db_ETL.list_collection_names()
#export to json
df_article_social.to_json('./article_social_seg.json',orient='index',force_ascii=False)
df_article_news.to_json('./article_news_seg.json',orient='index',force_ascii=False)
df_article_web.to_json('./article_web_seg.json',orient='index',force_ascii=False)
client.database_names()
db_ETL=client.ETL
#db_ETL.article_news_seg.drop()
#db_ETL.article_web_seg.drop()
#db_ETL.article_social_seg.drop()
#drop collection
#db.article_socialjson.drop()

