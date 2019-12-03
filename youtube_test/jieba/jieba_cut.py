import jieba
import json
import pandas as pd
import os

df=pd.read_excel(r'C:/Users/user/Desktop/project_test/youtube_crawl/text_file/video_df2ex_utf16.xlsx',encoding='utf-16')

n=len(df)
alltext=[]
stopset=set()
output=open('video_seg1101.txt','w',encoding='utf-8')

with open('C:/Users/user/Desktop/project_test/youtube_crawl/text_file/stop.txt','r',encoding='utf-8') as s:
    for line in s:
        stopset.add(line.strip('\n'))
jieba.load_userdict('userdict.txt')
for i in range(n):
    text= str(df.loc[i]['title'])+'\n'+str(df.loc[i]['description'])+'\n'+str(df.loc[i]['comment'])+'\n'
    cut=jieba.cut(text,cut_all=False)
    for j in cut:
        if j not in stopset:
            output.write(j+' ')
            alltext.append(list(j))
print(alltext)
output.close()
    
    