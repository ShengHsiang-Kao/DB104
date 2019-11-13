import pandas as pd
import os
import json
import jieba
import re
import xlsxwriter
from openpyxl import *
import operator
jieba.load_userdict('./userdict.txt')
df=pd.read_json(r'./Money101.json')

#

print(df)
# k=len(df)
# # # # print(k)
# wb_list=[]
# wc_list=[]
# for i in range(k):
#     ja=df['內文'][i]
#     gg=jieba.lcut(ja)
# # # # #     # print(gg)
#     wb_list.append(gg)
#     word_c={}
#     for i in gg:
#         if i in word_c:
#             word_c[i] +=1
#         else:
#             word_c[i] =1
#         word_cnt=[(k,word_c[k])for k in word_c]
#         word_cnt.sort(key=lambda x:x[1],reverse=True)
#     wc_list.append(word_cnt)
# # # # # print(wc_list)
# # # # # #
# # # # # # #
# df['斷詞']=wb_list
# df['詞頻']=wc_list
# # # # # #
# # print(df)
# # # # #
# df.to_json('Money101.json',orient='index',force_ascii=False)
#
# df.to_csv('Money101.csv',encoding='utf-8')
# df.to_excel('Money101.xlsx')
# # # # # #




# with open("./credix03.json") as g:
# 	result_data = json.load(g)
# print(type(result_data))
# # print(result_data[2])


# article_data =[]
# for n, each_article in enumerate(file_list):
#     article_path = source_file_path + '/' + each_article
#     with open(article_path, 'r', encoding = 'utf-8') as f:
#         tmp_article_string = f.read()
# print(tmp_article_string)