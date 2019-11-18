# 若為Mac電腦，請先貼上此段程式碼
########### For Mac user ###########
import os
import ssl
# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
####################################

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

headers = {'User-Agent' : str(random_header())}

#for i in range(0, 3):
url = 'https://www.dcard.tw/_api/forums/creditcard/posts?popular=false&limit=30&before=232004767'

res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')
#json_string = str(soup)
#js = json.loads(json_string)
print(soup)
    #
    # last_id = js[len(js)-1]['id']
    #
    # for each_article in js:
    #     print(each_article['title'])
    #     print('https://www.dcard.tw/f/creditcard/p/' + str(each_article['id']))
    #     print()
    #
    # url = 'https://www.dcard.tw/_api/forums/creditcard/posts?popular=false&limit=30&before=%s'%(last_id)