# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
print(items)
for item in items:
    question = item.find('h2').text()
    print('question',question)
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    with open('explore.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')





























