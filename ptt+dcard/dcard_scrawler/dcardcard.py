import requests
from bs4 import BeautifulSoup
import json
from my_fake_useragent import UserAgent
import os

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
resource_path = r'./DCTRY'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

for i in range(0, 10):
    url = 'https://www.dcard.tw/_api/forums/creditcard/posts?popular=false&limit=100&before=231776289'

    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    json_string = str(soup)
    js = json.loads(json_string)

    last_id = js[len(js)-1]['id']

    for each_article in js:
        print(each_article['title'])
        print('https://www.dcard.tw/f/creditcard/p/' + str(each_article['id']))
        print()

    url = 'https://www.dcard.tw/_api/forums/creditcard/posts?popular=false&limit=100&before=%s'%(last_id)