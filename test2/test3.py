# -*- coding: UTF-8 -*-
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

# r = requests.get("https://www.zhihu.com/explore", headers=headers)
r = requests.get("https://www.zhihu.com/explore")

pattern = re.compile('<a class="ExploreSpecialCard-contentTitle".*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)























