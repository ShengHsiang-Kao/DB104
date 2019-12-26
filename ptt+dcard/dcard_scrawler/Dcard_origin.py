from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time, re
from my_fake_useragent import UserAgent
import os
import json
import requests

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
#######################################################
resource_path = r'./DCtry'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

headers = {'User-Agent':str(random_header())}

# driver = Chrome('./chromedriver')
# driver.implicitly_wait(3)
# url = 'https://www.dcard.tw/f/graduate_school/'
# driver.get(url)
#
# for i in range(1, 40):
#     driver.execute_script('document.documentElement.scrollTop = document.documentElement.scrollHeight;')
#     time.sleep(5)
soup = BeautifulSoup(driver.page_source, features="html.parser")
nalr = soup.select('div[class="PostList_entry_1rq5Lf"] a[class="PostEntry_root_V6g0rd"]')
for j in nalr:
    #print(i.text+'\n')
    titurl = 'https://www.dcard.tw' + j['href']
    req2 = requests.get(titurl, headers=headers)
    soup2 = BeautifulSoup(req2.text, 'html.parser')
    content = soup2.select('div.Post_content_NKEl9d')
    content += soup2.select('span[class="Post_date_2ipeYS"] span')
    titname = soup2.select('h1[class="Post_title_2O-1el"]')
    print(titname)
    for t in titname:
        for n in content:
            print(n.text)
            print()
            # try:
            #     with open(r'./DCtry/%s.txt' % (t.text), 'a', encoding='utf-8') as f:
            #         f.write(n.text + '\n')
            # except:
            #     with open(r'./DCtry/article%s.txt' % (len(n)), 'a', encoding='utf-8') as f:
            #         f.write(n.text + '\n')
