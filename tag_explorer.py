import requests
from bs4 import BeautifulSoup
import json
import re
import random
from requests_html import HTMLSession

with open('tags_list.json', 'r') as f:
    tags_list = json.load(f)
url = 'https://www.amazon.com/dp/B085VKW7MK'


HEADERS_LIST = [
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre",
]

session = requests.Session()
header = {
        "User-Agent": random.choice(HEADERS_LIST),
    "X-Requested-With": "XMLHttpRequest",
}
session.headers.update(header)


resp = session.get(url)
print(resp)

print(resp.text.find('c1.adform.net'))

# for tag in tags_list:
#     for url in tag['tag_urls']:
#         print(url.strip())

