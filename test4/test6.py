# -*- coding: UTF-8 -*-
import json

str = '''
[{
    "name": "王伟",
    "gender": "男",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
# print(type(str))
data = json.loads(str)
# print(data)
# print(type(data))
# print(data[0]['name'])
# print(data[0].get('name'))
# print(data[0].get('age'))
# print(data[0].get('age', 25))
print(json.dumps(data, indent=2, ensure_ascii=False))































