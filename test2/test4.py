# -*- coding: UTF-8 -*-
import requests

r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)
with open("data/favicon.ico", 'wb') as f:
    f.write(r.content)
































