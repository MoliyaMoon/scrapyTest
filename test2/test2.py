# -*- coding: UTF-8 -*-
import requests

data = {
    'name':'germey',
    'age':'22'
}
r = requests.get("http://httpbin.org/get")
print(type(r.text))
print(r.json())
print(type(r.json()))
