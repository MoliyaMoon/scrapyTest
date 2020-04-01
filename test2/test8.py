# -*- coding: UTF-8 -*-

import requests

files = {'file': open('data/favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)































