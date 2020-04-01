# -*- coding: UTF-8 -*-
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import traceback

page = 1

base_url = 'http://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(since_id):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
    }
    global page
    if page > 1:
        params['since_id'] = since_id
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page += 1
            return response.json()
    except requests.ConnectionError as e:
        print('Error: ', e.args)

def parse_page(json):
    if json:
        try:
            since_id = json.get('data').get('cardlistInfo').get('since_id')
        except:
            traceback.print_exc()
            print("end get data, since-id wrong")
            exit()
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

if __name__ == '__main__':
    while page



























