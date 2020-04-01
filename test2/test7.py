# -*- coding: UTF-8 -*-

import requests

r = requests.get('http://www.jianshu.com')
print(r.status_code)
exit() if not r.status_code == requests.codes.not_found else print('Request Successfully')































