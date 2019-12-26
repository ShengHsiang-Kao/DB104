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
#         print(article_text)
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
    k.loc[index]= index+1,article_title,article_time,title_url,article_text
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
    synonym_dict[each_row.split(',')[0]]=[item for item in each_row.split(',')] 

synonym_list=[]
for i in syn_str:
    each_word=i.split(',')
    synonym_list += each_word
# print(synonum_list)
for word_tmp in k['斷詞']:
    for num, i in enumerate(word_tmp):
        for key in synonym_dict:
            for word_value in synonym_dict[key]:
                if i == word_value:
                    word_tmp[num] = key
# print(k['斷詞'][317])
# re-join to article after replacing synonym
for i in range(len(k['斷詞'])):
    k['內文'][i]=''.join(k['斷詞'][i])
print(k['內文'][993])

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
df_3=pd.read_json(r'./dcard_creditcard.json')
df_3

# +
bank={'中信':'中信','中國信託':'中信' ,'中信金':'中信' ,'中信金控':'中信','中信銀':'中信',
'玉山':'玉山','玉山金':'玉山','玉山金控':'玉山','玉山銀':'玉山',
'Richart':'Richart', 'richart':'Richart',
'KOKO':'KOKO','koko':'KOKO',
'國泰':'國泰','國泰世華':'國泰','國泰金':'國泰','國泰金控':'國泰',
'台新':'台新','台新金':'台新','台新金控':'台新','台新銀':'台新','台新銀行':'台新',
'永豐':'永豐','永豐銀':'永豐','永豐金':'永豐','永豐金控':'永豐','永豐銀行':'永豐',
'兆豐':'兆豐','兆豐銀':'兆豐','兆豐金':'兆豐','兆豐金控':'兆豐','兆豐銀行':'兆豐',
'花旗':'花旗','花旗銀':'花旗','花旗銀行':'花旗',
'一銀':'一銀','第一銀':'一銀','第一金':'一銀','第一金控':'一銀','第一銀行':'一銀',
'富邦':'富邦','富邦金':'富邦','富邦金控':'富邦','富邦銀':'富邦','富邦銀行':'富邦',
'彰化':'彰化','彰化銀':'彰化','彰化金控':'彰化','彰化金':'彰化','彰化銀行':'彰化',
'新光':'新光','新光銀':'新光','新光金':'新光','新光金控':'新光','新光銀行':'新光',
'匯豐':'匯豐','匯豐銀行':'匯豐','匯豐銀':'匯豐',
'陽信銀行':'陽信','陽信':'陽信','陽信銀':'陽信',
'元大':'元大','元大銀行':'元大','元大金控':'元大','元大銀':'元大',
'星展':'星展','星展銀行':'星展','星展銀':'星展','DBS':'星展','dbs':'星展',
'渣打':'渣打','渣打銀行':'渣打','渣打銀':'渣打',
'上海商銀':'上海商銀','上海銀行':'上海商銀','上海商業':'上海商銀',
'華南':'華南','華南銀行':'華南','華南金控':'華南','華南銀':'華南',
'凱基':'凱基','凱基銀行':'凱基','凱基金控':'凱基',
'合作金庫':'合作金庫','合庫':'合作金庫',
'王道':'王道','王道銀行':'王道',
'澳盛':'澳盛','澳盛銀行':'澳盛','ANZ':'澳盛','anz':'澳盛',
'遠東商銀':'遠東商銀','遠銀':'遠東商銀','遠東銀':'遠東商銀',
'土地銀行':'土地','土銀':'土地',
'聯邦銀行':'聯邦','聯邦':'聯邦',
'台灣銀行':'臺灣銀行','臺灣銀行':'臺灣銀行',
'京城':'京城','京城銀行':'京城',
'日盛':'日盛','日盛銀行':'日盛',
'華泰':'華泰','華泰銀行':'華泰',
'台中銀行':'台中銀行','台中銀':'台中銀行',
'高雄銀行':'高雄銀行','高雄銀':'高雄銀行',
'台灣企銀':'臺灣企銀','臺灣企銀':'臺灣企銀','臺企銀':'臺灣企銀',
'瑞興銀行':'瑞興銀行','瑞興':'瑞興銀行',}

behavior={'跑步':'運動','健身房':'運動','運動':'運動',
'旅遊':'旅遊','旅行':'旅遊','機票':'旅遊','飯店':'旅遊','機場':'旅遊','出國':'旅遊',
'保險':'保險','保費':'保險',
'加油':'加油','中油':'加油',
'國外':'國外','海外':'國外',
'電影':'電影','國賓':'電影','威秀':'電影',
'網購':'網購' ,'網拍':'網購', '蝦皮':'網購', '電商':'網購','pchome':'網購','PChome':'網購','Yahoo':'網購','momo':'網購','MOMO':'網購',
'行動支付':'行動支付','PI錢包':'行動支付','pi錢包':'行動支付','街口':'行動支付','Pi錢包':'行動支付','拍錢包':'行動支付',
'新光三越':'百貨','SOGO':'百貨','sogo':'百貨','遠百':'百貨','遠東百貨':'百貨',
'紅利點數':'紅利','紅利兌換':'紅利',
'超商':'超商','7-11':'超商','全家':'超商','全家便利':'超商','萊爾富':'超商','OK便利':'超商',
'屈臣氏':'藥妝','康是美':'藥妝',
'大潤發':'量販店','家樂福':'量販店','愛買':'量販店',
'全聯':'超市','頂好':'超市',
'哩程':'航空哩程','航空哩程':'航空哩程'}

card={'linepay':'LINEPay','Linepay':'LINEPay','LinePay':'LINEPay','LINEPAY':'LINEPay','LINE PAY':'LINEPay','Line pay':'LINEPay',
'line pay':'LINEPay','Line':'LINEPay','LINE':'LINEPay','line':'LINEPay',
'GOGO':'GoGo','gogo':'GoGo','黑狗':'GoGo','黑狗卡':'GoGo','gogo卡':'GoGo','GOGO卡':'GoGo','Gogo卡':'GoGo','Gogo':'GoGo','GoGo':'GoGo',
'flygo':'Flygo','Flygo':'Flygo','FLYGO':'Flygo','飛狗':'Flygo','飛狗卡':'Flygo','FlyGo':'Flygo','fly':'Flygo',
'大戶':'dawho','dawho':'dawho','Dawho':'dawho','DAWHO':'dawho',
'PI':'Pi','Pi':'Pi','pi卡':'Pi','PI卡':'Pi',
'ubear':'Ubear','UBEAR':'Ubear','Ubear':'Ubear','ubear':'Ubear','bear':'Ubear','BEAR':'Ubear',
'u bear':'Ubear','U bear':'Ubear','u bear':'Ubear', 'Ubear卡':'Ubear','U Bear':'Ubear',
'only':'Only','ONLY':'Only','Only':'Only',
'賴點':'賴點卡','賴點卡':'賴點卡', 
'酷玩卡':'酷玩卡','酷玩卡':'酷玩卡',
'饗樂':'饗樂卡','饗樂卡':'饗樂卡',
'koko':'KOKO','KOKO':'KOKO','KoKo':'KOKO','Koko':'KOKO',
'星燦':'星燦卡','星燦卡':'星燦卡','星璨':'星燦卡',
'統一獅':'統一獅聯名卡',
'中信兄弟':'中信兄弟聯名卡',
'富邦悍將':'富邦悍將聯名卡',
'My樂現金回饋卡':'My樂現金回饋卡','My樂現金回饋':'My樂現金回饋卡',
'哆啦A夢JCB聯名卡':'哆啦A夢JCB聯名卡','哆啦A夢':'哆啦A夢JCB聯名卡',
'Omiyage':'Omiyage','omiyage':'Omiyage',
'尊御世界卡':'尊御世界卡',
'鑽金一卡通聯名卡':'鑽金','鑽金':'鑽金',
'炫晶御璽卡':'炫晶御璽卡','炫晶卡':'炫晶御璽卡','炫晶':'炫晶御璽卡',
'現金回饋御璽卡':'現金回饋御璽卡',
'PChome Prime聯名卡':'PChome Prime聯名卡','Prime聯名卡':'PChome Prime聯名卡','Prime':'PChome Prime聯名卡','rime':'PChome Prime聯名卡',
'購物聯名卡':'蝦皮購物聯名卡','蝦皮聯名':'蝦皮購物聯名卡','蝦皮卡':'蝦皮購物聯名卡','國泰世華蝦皮卡':'蝦皮購物聯名卡',
'Lamigo聯名卡':'Lamigo聯名卡','Lamigo':'Lamigo聯名卡','lamigo':'Lamigo聯名卡',
'SPORT卡':'SPORT卡','SPORT':'SPORT卡',
'e秒刷鈦金卡':'e秒刷鈦金卡','e秒刷':'e秒刷鈦金卡',
'小小兵信用卡':'小小兵信用卡','小小兵':'小小兵信用卡',
'everyday鈦金卡':'everyday鈦金卡','everyday':'everyday鈦金卡',
'街口聯名卡':'街口聯名卡','街口聯名':'街口聯名卡',
'Gogoro聯名卡':'Gogoro聯名卡','Gogoro':'Gogoro聯名卡','gogoro':'Gogoro聯名卡',
'現金回饋御璽卡':'現金回饋御璽卡',
'簡單卡':'簡單卡',
'數位生活':'數位生活卡',
'美國運通':'美國運通','法拉利':'法拉利無限卡',
'omiyage':'Omiyage','OMIYAGE':'Omiyage','omiyage':'Omiyage',
'e秒刷鈦金卡':'e秒刷鈦金卡','e秒刷':'e秒刷鈦金卡',
'南開科技大學認同卡':'南開科技大學認同卡',
'聯邦OTA手機信用卡':'聯邦OTA手機信用卡',
'魔法少女iPASS一卡通聯名卡':'魔法少女iPASS一卡通聯名卡',
'富邦鑽保卡':'富邦鑽保卡',
'行遍天下聯名卡':'行遍天下聯名卡',
'幸運鈦金卡':'幸運鈦金卡',
'昇恒昌聯名卡':'昇恒昌聯名卡',
'新光三越一卡通聯名卡':'新光三越一卡通聯名卡',
'悠遊晶緻卡':'悠遊晶緻卡',
'鈦金商務卡':'鈦金商務卡',
'永豐Me Card':'永豐Me Card',
'永豐鈦豐卡':'永豐鈦豐卡',
'利倍卡':'利倍卡',
'富邦財神卡':'富邦財神卡',
'八福公益卡':'八福公益卡',
'台灣銀行':'台灣銀行',
'F1加油卡':'F1加油卡',
'全家Fish悠遊聯名卡':'全家Fish悠遊聯名卡',
'新光銀行寰宇卡':'新光銀行寰宇卡',
'建築師無限卡':'建築師無限卡',
'icash聯名卡':'icash聯名卡',
'世界卡(icash)':'世界卡(icash)',
'玉山教師卡':'玉山教師卡',
'安泰銀行信用卡':'安泰銀行信用卡',
'寰宇現金回饋卡':'寰宇現金回饋卡',
'合作金庫無限卡':'合作金庫無限卡',
'合庫雙幣信用卡(日圓)':'合庫雙幣信用卡(日圓)',
'一卡通聯名卡':'一卡通聯名卡',
'TAIPEI 101 聯名卡':'TAIPEI 101 聯名卡',
'公務人員國民旅遊卡':'公務人員國民旅遊卡',
'C’est Moi我的卡':'C’est Moi我的卡',
'Super Life 卡':'Super Life 卡',
'聯邦銀行無限卡':'聯邦銀行無限卡',
'匯豐銀行白金卡':'匯豐銀行白金卡',
'樂活Visapaywave感應式白金卡':'樂活Visapaywave感應式白金卡',
'臺北科大愛校認同卡':'臺北科大愛校認同卡',
'新光三越icash聯名卡':'新光三越icash聯名卡',
'鈦金悠遊聯名卡':'鈦金悠遊聯名卡',
'公司戶商務卡':'公司戶商務卡',
'樂享晶緻卡(原大眾)':'樂享晶緻卡(原大眾)',
'華歌爾聯名卡':'華歌爾聯名卡',
'高雄going鈦金卡':'高雄going鈦金卡',
'長庚紀念醫院悠遊認同卡':'長庚紀念醫院悠遊認同卡',
'樂購卡':'樂購卡',
'雙幣信用卡':'雙幣信用卡',
'鈦金商旅卡':'鈦金商旅卡',
'大台北商銀聯名卡':'大台北商銀聯名卡',
'KOKOicash聯名卡':'KOKOicash聯名卡',
'商務卡':'商務卡',
'商旅鈦金卡商務':'商旅鈦金卡商務',
'花蓮一信聯名卡':'花蓮一信聯名卡',
'元大白金卡':'元大白金卡',
'燦坤生活一卡通聯名卡':'燦坤生活一卡通聯名卡',
'圓山大飯店一卡通聯名卡':'圓山大飯店一卡通聯名卡',
'鹿港天后宮晶緻一卡通認同卡':'鹿港天后宮晶緻一卡通認同卡',
'台塑(一卡通)聯名卡':'台塑(一卡通)聯名卡',
'ANA聯名卡':'ANA聯名卡',
'日盛銀行-無限卡':'日盛銀行-無限卡',
'台中二信聯名卡':'台中二信聯名卡',
'一銀卡御守系列':'一銀卡御守系列',
'台灣國際基督教會認同卡':'台灣國際基督教會認同卡',
'NFC 手機信用卡':'NFC 手機信用卡',
'雅芳聯名卡':'雅芳聯名卡',
'哆啦A夢晶緻卡':'哆啦A夢晶緻卡',
'NFC手機信用卡':'NFC手機信用卡',
'北港朝天宮認同卡':'北港朝天宮認同卡',
'元大鈦金卡':'元大鈦金卡',
'COSTCO聯名卡':'COSTCO聯名卡',
'元大Life卡':'元大Life卡',
'中興保全聯名卡':'中興保全聯名卡',
'合作金庫世界卡':'合作金庫世界卡',
'學學認同卡':'學學認同卡',
'哆啦A夢卡':'哆啦A夢卡',
'歐付寶悠遊聯名卡':'歐付寶悠遊聯名卡',
'一卡通聯名晶緻卡':'一卡通聯名晶緻卡',
'幸福卡':'幸福卡',
'鈦金商旅卡':'鈦金商旅卡',
'中油職工福利認同卡':'中油職工福利認同卡',
'臺灣大學卡':'臺灣大學卡',
'悠遊聯名卡':'悠遊聯名卡',
'澳盛現金回饋卡':'澳盛現金回饋卡',
'中華郵政工會認同卡':'中華郵政工會認同卡',
'彰化六信聯名卡':'彰化六信聯名卡',
'玉山雙幣信用卡':'玉山雙幣信用卡',
'京城銀行聯名卡':'京城銀行聯名卡',
'頂好超市聯名卡':'頂好超市聯名卡',
'高雄醫學院認同卡':'高雄醫學院認同卡',
'美元雙幣信用卡':'美元雙幣信用卡',
'世界卡':'世界卡',
'聯邦銀行世界卡':'聯邦銀行世界卡',
'環球無限卡':'環球無限卡',
'高雄觀光福利聯名卡':'高雄觀光福利聯名卡',
'中國信託紅利卡':'中國信託紅利卡',
'元大鑽金icash聯名卡':'元大鑽金icash聯名卡',
'佐登妮絲聯名卡':'佐登妮絲聯名卡',
'故宮之友卡':'故宮之友卡',
'媚儷鈦金卡':'媚儷鈦金卡',
'台塑(悠遊)聯名卡':'台塑(悠遊)聯名卡',
'聯邦樂活一卡通聯名卡':'聯邦樂活一卡通聯名卡',
'三信商業銀行信用卡':'三信商業銀行信用卡',
'玉山eTag悠遊聯名卡':'玉山eTag悠遊聯名卡',
'分期便利卡':'分期便利卡',
'大潤發油樂聯名卡':'大潤發油樂聯名卡',
'玫瑰卡':'玫瑰卡',
'LOVE晶緻悠遊聯名卡－寵愛紅卡':'LOVE晶緻悠遊聯名卡－寵愛紅卡',
'元大台灣霹靂卡':'元大台灣霹靂卡',
'世界商務卡':'世界商務卡',
'超級現金回饋卡':'超級現金回饋卡',
'個人商旅卡':'個人商旅卡',
'聯邦旅遊卡':'聯邦旅遊卡',
'Gogoro聯名卡':'Gogoro聯名卡',
'利high卡':'利high卡',
'淡水信用合作社聯名卡':'淡水信用合作社聯名卡',
'ｉ網購生活卡':'ｉ網購生活卡',
'哆啦A夢悠遊聯名卡':'哆啦A夢悠遊聯名卡',
'花旗現金回饋(悠遊)卡':'花旗現金回饋(悠遊)卡',
'頂好Visa payWave聯名卡':'頂好Visa payWave聯名卡',
'享購鈦金卡':'享購鈦金卡',
'台灣黑熊認同卡':'台灣黑熊認同卡',
'酷比悠遊聯名卡':'酷比悠遊聯名卡',
'玉山晶緻悠遊卡':'玉山晶緻悠遊卡',
'商旅卡':'商旅卡',
'日盛ALL PASS卡':'日盛ALL PASS卡',
'商務白金卡':'商務白金卡',
'原子小金剛悠遊聯名卡':'原子小金剛悠遊聯名卡',
'藝術白金卡':'藝術白金卡',
'iCash愛現':'iCash愛現',
'日盛GOGO加油卡':'日盛GOGO加油卡',
'雙幣鈦金商旅卡':'雙幣鈦金商旅卡',
'台南三信聯名卡':'台南三信聯名卡',
'鹿港天后宮鈦金悠遊認同卡':'鹿港天后宮鈦金悠遊認同卡',
'新光銀行分期7卡':'新光銀行分期7卡',
'Hello Kitty分享聯名卡商務':'Hello Kitty分享聯名卡商務',
'iCash聯名卡':'iCash聯名卡',
'中國人壽聯名卡':'中國人壽聯名卡',
'Combo晶片卡':'Combo晶片卡',
'國泰人壽聯名卡':'國泰人壽聯名卡',
'永豐財富無限卡':'永豐財富無限卡',
'澎湖戀戀菊島認同卡':'澎湖戀戀菊島認同卡',
'銀色之愛鈦商卡':'銀色之愛鈦商卡',
'樂活卡(原澳盛)':'樂活卡(原澳盛)',
'愛Pass鈦金卡':'愛Pass鈦金卡',
'幸福御守卡／粉':'幸福御守卡／粉',
'大甲媽祖認同卡':'大甲媽祖認同卡',
'微風廣場 JSpeedy感應式聯名卡':'微風廣場 JSpeedy感應式聯名卡',
'e秒萬事通金融信用卡':'e秒萬事通金融信用卡',
'台灣企銀商務卡':'台灣企銀商務卡',
'國民旅遊卡':'國民旅遊卡',
'金采卡':'金采卡',
'燦坤生活聯名卡':'燦坤生活聯名卡',
'運籌理財信用卡':'運籌理財信用卡',
'台北市第五信用合作社聯名卡':'台北市第五信用合作社聯名卡',
'元大樂遊卡':'元大樂遊卡',
'鑑賞家白金卡':'鑑賞家白金卡',
'大立無限卡':'大立無限卡',
'輔仁大學認同卡':'輔仁大學認同卡',
'天仁茗茶聯名卡':'天仁茗茶聯名卡',
'SunnyCard':'SunnyCard',
'華歌爾鈦金悠遊聯名卡':'華歌爾鈦金悠遊聯名卡',
'Hello Kitty點數聯名卡商務':'Hello Kitty點數聯名卡商務',
'台新財富無限卡':'台新財富無限卡',
'卡娜赫拉的小動物icash聯名卡':'卡娜赫拉的小動物icash聯名卡',
'勞動保障信用卡':'勞動保障信用卡',
'醫師尊榮無限卡':'醫師尊榮無限卡',
'里仁為美福智卡':'里仁為美福智卡',
'元大商務鈦金卡':'元大商務鈦金卡',
'新竹市民認同卡':'新竹市民認同卡',
'逢甲人一卡通鈦金認同卡':'逢甲人一卡通鈦金認同卡',
'遠傳friDay聯名卡':'遠傳friDay聯名卡',
'麗寶悠遊聯名卡':'麗寶悠遊聯名卡',
'玉山銀行卡':'玉山銀行卡',
'元大鑽金卡':'元大鑽金卡',
'無限卡':'無限卡',
'Hello Kitty鑽金聯名卡商務':'Hello Kitty鑽金聯名卡商務',
'漢神百貨聯名卡':'漢神百貨聯名卡',
'富邦數位生活卡':'富邦數位生活卡',
'國璽聯名卡':'國璽聯名卡',
'HappyCash & HAPPY GO聯名卡':'HappyCash & HAPPY GO聯名卡',
'玉山教師鈦金卡':'玉山教師鈦金卡',
'FlyGo商務':'FlyGo商務',
'白金商旅卡':'白金商旅卡',
'錢進卡':'錢進卡',
'飲食男女聯名卡':'飲食男女聯名卡',
'NISSAN感心悠遊聯名卡':'NISSAN感心悠遊聯名卡',
'中華溫馨服務卡':'中華溫馨服務卡',
'樂活悠遊鈦金卡':'樂活悠遊鈦金卡',
'京華城聯名卡':'京華城聯名卡',
'台灣企銀信用卡':'台灣企銀信用卡',
'MUJI無印良品聯名卡':'MUJI無印良品聯名卡',
'台大EMBA基金會白金卡':'台大EMBA基金會白金卡',
'富邦尊御世界卡':'富邦尊御世界卡',
'美福聯名卡':'美福聯名卡',
'玉山統一時代悠遊聯名卡':'玉山統一時代悠遊聯名卡',
'永豐國民旅遊卡':'永豐國民旅遊卡',
'新光三越聯名卡':'新光三越聯名卡',
'士林高商校友認同卡':'士林高商校友認同卡',
'NewCentury無限卡':'NewCentury無限卡',
'中醫師無限卡':'中醫師無限卡',
'旅鑽個人商務信用卡':'旅鑽個人商務信用卡',
'元大鑽金一卡通聯名卡':'元大鑽金一卡通聯名卡',
'信望愛認同卡':'信望愛認同卡',
'鼎極卡':'鼎極卡',
'華銀白金卡':'華銀白金卡',
'SPORT卡商務':'SPORT卡商務',
'鼎鑽財富無限卡':'鼎鑽財富無限卡',
'嘉義三信聯名卡':'嘉義三信聯名卡',
'愛心卡':'愛心卡',
'農金一卡通聯名卡':'農金一卡通聯名卡',
'中華航空聯名卡':'中華航空聯名卡',
'兆豐悠遊聯名卡':'兆豐悠遊聯名卡',
'雙幣鈦金商旅卡':'雙幣鈦金商旅卡',
'幸福加值卡':'幸福加值卡',
'桐花認同卡':'桐花認同卡',
'新光三越悠遊聯名卡':'新光三越悠遊聯名卡',
'清華大學悠遊認同卡':'清華大學悠遊認同卡',
'VOLVO汽車聯名卡':'VOLVO汽車聯名卡',
'亞洲無限卡':'亞洲無限卡',
'聯邦農金聯名卡':'聯邦農金聯名卡',
'亞洲微創手術中心認同卡':'亞洲微創手術中心認同卡',
'大買家油樂聯名卡':'大買家油樂聯名卡',
'台灣大哥大悠遊聯名卡':'台灣大哥大悠遊聯名卡',
'ETC聯名卡':'ETC聯名卡',
'原子小金剛卡':'原子小金剛卡',
'享利白金卡':'享利白金卡',
'Bankee卡':'Bankee卡',
'兆豐世界卡':'兆豐世界卡',
'耐斯廣場NP聯名卡':'耐斯廣場NP聯名卡',
'萬事通悠遊金融信用卡':'萬事通悠遊金融信用卡',
'富多卡':'富多卡',
'ｉ網購生活卡':'ｉ網購生活卡',
'台塑(一卡通)聯名卡商務':'台塑(一卡通)聯名卡商務',
'哆啦A夢悠遊晶緻卡':'哆啦A夢悠遊晶緻卡',
'大甲媽祖悠遊認同卡':'大甲媽祖悠遊認同卡',
'玉山雙幣信用卡':'玉山雙幣信用卡',
'獅子之友認同卡':'獅子之友認同卡',
'太陽卡':'太陽卡',
'農金悠遊聯名卡':'農金悠遊聯名卡',
'理財型白金卡':'理財型白金卡',
'東海大學悠遊認同卡':'東海大學悠遊認同卡',
'導盲犬認同卡':'導盲犬認同卡',
'桃園市市民卡聯名信用卡':'桃園市市民卡聯名信用卡',
'比漾聯名卡':'比漾聯名卡',
'Global Mall聯名卡':'Global Mall聯名卡',
'KOKO COMBO icash':'KOKO COMBO icash',
'夢時代icash 聯名卡':'夢時代icash 聯名卡',
'陽信鈦金卡':'陽信鈦金卡',
'VOGUE聯名卡':'VOGUE聯名卡',
'NFC手機信用卡':'NFC手機信用卡',
'現金回饋悠遊鈦金卡':'現金回饋悠遊鈦金卡',
'Display金融信用卡':'Display金融信用卡',
'信義房屋聯名卡':'信義房屋聯名卡',
'現金回饋悠遊鈦金Combo卡':'現金回饋悠遊鈦金Combo卡',
'微風廣場Visa Pay Wave感應式聯名卡':'微風廣場Visa Pay Wave感應式聯名卡',
'陽信櫻花白金卡':'陽信櫻花白金卡',
'微風聯名卡':'微風聯名卡',
'行動鈦金卡':'行動鈦金卡',
'玉山統一時代icash聯名卡':'玉山統一時代icash聯名卡',
'NFC寰宇鈦商手機信用卡':'NFC寰宇鈦商手機信用卡',
'家扶公益認同卡':'家扶公益認同卡',
'花旗HAPPY GO聯名卡':'花旗HAPPY GO聯名卡',
'美樂家生活卡':'美樂家生活卡',
'兆豐無限卡':'兆豐無限卡',
'手機信用卡':'手機信用卡',
'ESPRIT聯名卡':'ESPRIT聯名卡',
'樂天信用卡':'樂天信用卡',
'晶片Combo card':'晶片Combo card',
'一卡通聯名鈦金卡':'一卡通聯名鈦金卡',
'棉花田悠遊聯名卡':'棉花田悠遊聯名卡',
'新世代信用卡':'新世代信用卡',
'中國醫藥大學暨附設醫院晶緻認同卡':'中國醫藥大學暨附設醫院晶緻認同卡',
'Combo Life卡':'Combo Life卡',
'遠東HAPPY GO頂級信用卡':'遠東HAPPY GO頂級信用卡',
'南紡夢時代聯名卡':'南紡夢時代聯名卡',
'永豐Me Display Card':'永豐Me Display Card',
'分享卡':'分享卡',
'中華電信感恩卡':'中華電信感恩卡',
'微風悠遊聯名卡':'微風悠遊聯名卡',
'經典鈦金卡':'經典鈦金卡',
'I-FIRST生活卡':'I-FIRST生活卡',
'雙幣鈦金商旅卡':'雙幣鈦金商旅卡',
'C’est Moi旅遊悠遊卡':'C’est Moi旅遊悠遊卡',
'中興大學認同卡':'中興大學認同卡',
'大葉高島屋聯名卡':'大葉高島屋聯名卡',
'TheShoppingCard分期卡':'TheShoppingCard分期卡',
'NewCentury世界卡':'NewCentury世界卡',
'新光銀行世界卡':'新光銀行世界卡',
'中華電信商務鈦金感恩卡':'中華電信商務鈦金感恩卡',
'澎湖iPASS卡':'澎湖iPASS卡',
'LOVE晶緻悠遊聯名卡－酷愛黑卡':'LOVE晶緻悠遊聯名卡－酷愛黑卡',
'合庫雙幣信用卡':'合庫雙幣信用卡',
'台塑(悠遊)聯名卡商務':'台塑(悠遊)聯名卡商務',
'富貴無限卡':'富貴無限卡',
'美安悠遊聯名卡':'美安悠遊聯名卡',
'山隆優油卡':'山隆優油卡',
'金采鈦商卡':'金采鈦商卡',
'順發多謝聯名卡':'順發多謝聯名卡',
'MAZDA天空卡':'MAZDA天空卡',
'i-Fun愛玩樂卡':'i-Fun愛玩樂卡',
'凱基無限卡':'凱基無限卡',
'板信銀行聯名卡':'板信銀行聯名卡',
'葡眾聯名卡':'葡眾聯名卡',
'幸運PLUS鈦金卡':'幸運PLUS鈦金卡',
'大紀元認同卡':'大紀元認同卡',
'富邦財神手機卡':'富邦財神手機卡',
'得利COMBO晶片卡':'得利COMBO晶片卡',
'白沙屯拱天宮媽祖認同卡':'白沙屯拱天宮媽祖認同卡',
'HappyCash & HAPPY GO聯名卡':'HappyCash & HAPPY GO聯名卡',
'民間版國民旅遊卡':'民間版國民旅遊卡',
'鈦豐卡':'鈦豐卡',
'玩全南投認同卡':'玩全南投認同卡',
'宜蘭大學悠遊認同卡':'宜蘭大學悠遊認同卡',
'聯邦國民旅遊卡':'聯邦國民旅遊卡',
'Sweet Home白金卡':'Sweet Home白金卡',
'ｉ網購生活卡':'ｉ網購生活卡',}
# -

df_3
df_3.loc['銀行']=None
df_3.loc['卡片']=None
df_3.loc['行為']=None
df_3
len(df_3.columns)

for article in range(len(df_3.columns)):
    article_bank={}
    for word in df_3.loc['斷詞'][article]:
        if word in bank:
            if bank[word] not in article_bank:
                article_bank[bank[word]] = 1
            else:
                article_bank[bank[word]] += 1
    print(article_bank)
    df_3.loc['銀行'][article]=article_bank   

for article in range(len(df_3.columns)):
    article_card={}
    for word in df_3.loc['斷詞'][article]:
        if word in card:
            if card[word] not in article_card:
                article_card[card[word]] = 1
            else:
                article_card[card[word]] += 1
    print(article_card)
    df_3.loc['卡片'][article]=article_card   

for article in range(len(df_3.columns)):
    article_behavior={}
    for word in df_3.loc['斷詞'][article]:
        if word in behavior:
            if behavior[word] not in article_behavior:
                article_behavior[behavior[word]] = 1
            else:
                article_behavior[behavior[word]] += 1
    print(article_behavior)
    df_3.loc['行為'][article]=article_behavior   

df_3

df_3.to_json(r'./dcard_tag.json', orient='index', force_ascii=False)

import xlsxwriter
writer = pd.ExcelWriter('dcard_tag.xlsx', engine='xlsxwriter')
df_3.to_excel(writer, sheet_name='Sheet1')
writer.save()
