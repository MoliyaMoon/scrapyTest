# -*- coding: UTF-8 -*-
import requests
from requests import exceptions
import re
import json
import os
import time


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException as e:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?"name"><a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].replace("\n", "").strip(),
            'time': item[4].split("：")[1].strip(),
            'score': item[5].strip() + item[6],
        }

def write_to_json(content, filename):
    with open(filename, 'a') as f:
        print(json.dumps(content, ensure_ascii=False,))
        f.write(json.dumps(content, ensure_ascii=False,) + "\n")

def main(filename, index):
    url = 'http://maoyan.com/board/4?offset=' + str(index)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        write_to_json(item, filename)


if __name__ == '__main__':
    filename = 'data/result.txt'
    if os.path.exists(filename):
        os.remove(filename)
    for i in range(10):
        main(filename, index=i * 10)
        time.sleep(1)































