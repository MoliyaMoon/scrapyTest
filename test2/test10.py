# -*- coding: UTF-8 -*-

import requests

# headers = {
#     'Cookie': '_zap=9dc4bfb4-8151-498b-a321-a51e25cb9668; d_c0="AJDjUy5PHQ-PTpf4mydc-lTg8gRf1f47STs=|1552444951"; _xsrf=628749ef-e5da-4584-ae5d-17d9f8f74eef; l_n_c=1; n_c=1; __utmc=51854390; __utmv=51854390.000--|3=entry_date=20190313=1; _ga=GA1.2.1673360431.1581927519; q_c1=cce4e048fcb34c788bfaa5981e48f461|1584688197000|1552444952000; r_cap_id="M2JmYzk4YzE1YjYwNGFkOWFjYzhlNTMwZDUwMTY2OGI=|1584688197|85a96f5fa3547f032487a8e793556a933ae96d0e"; cap_id="NTRkYjZkODljY2M0NGRlZGI1YTZmMTUxYmUzOTk0Yjg=|1584688197|25f3baf94b22bbb02c271e577f32685408be92b2"; l_cap_id="M2I2NTI2NTlkODQ2NDUyM2JmZTViMmY2MzdjZDAwNmU=|1584688197|6e4471255e5eb63886cd46b4e6714b6cdc7760cc"; __utma=51854390.1673360431.1581927519.1581927519.1584688200.2; __utmz=51854390.1584688200.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _gid=GA1.2.1518447763.1585118647; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1585118656,1585124616,1585124776,1585125426; capsion_ticket="2|1:0|10:1585189698|14:capsion_ticket|44:NGFiNTZmNWJkNjVhNDhkNGJmYmI0Yjg5NmI0ZTM5ZGI=|2e0b8b7c1103b867db15188dcdbfbc6126c845d412a8ef84b57b59dd2ee04fc7"; z_c0="2|1:0|10:1585189717|4:z_c0|92:Mi4xYVNpN0FnQUFBQUFBa09OVExrOGREeVlBQUFCZ0FsVk5WV0ZwWHdDelozbjIxX19WSjNXNWZLNDNrQ29yd0NsRGxn|ccb6f7fa59996f6e94b47479e0438da237bbc9d88372d13c66233f4cc169616e"; _gat_gtag_UA_149949619_1=1; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585203777; KLBRSID=ca494ee5d16b14b649673c122ff27291|1585203778|1585203773',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
# }
#
# r = requests.get("https://www.zhihu.com", headers=headers)
# print(r.text)

cookies = '_zap=9dc4bfb4-8151-498b-a321-a51e25cb9668; d_c0="AJDjUy5PHQ-PTpf4mydc-lTg8gRf1f47STs=|1552444951"; _xsrf=628749ef-e5da-4584-ae5d-17d9f8f74eef; l_n_c=1; n_c=1; __utmc=51854390; __utmv=51854390.000--|3=entry_date=20190313=1; _ga=GA1.2.1673360431.1581927519; q_c1=cce4e048fcb34c788bfaa5981e48f461|1584688197000|1552444952000; r_cap_id="M2JmYzk4YzE1YjYwNGFkOWFjYzhlNTMwZDUwMTY2OGI=|1584688197|85a96f5fa3547f032487a8e793556a933ae96d0e"; cap_id="NTRkYjZkODljY2M0NGRlZGI1YTZmMTUxYmUzOTk0Yjg=|1584688197|25f3baf94b22bbb02c271e577f32685408be92b2"; l_cap_id="M2I2NTI2NTlkODQ2NDUyM2JmZTViMmY2MzdjZDAwNmU=|1584688197|6e4471255e5eb63886cd46b4e6714b6cdc7760cc"; __utma=51854390.1673360431.1581927519.1581927519.1584688200.2; __utmz=51854390.1584688200.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _gid=GA1.2.1518447763.1585118647; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1585118656,1585124616,1585124776,1585125426; capsion_ticket="2|1:0|10:1585189698|14:capsion_ticket|44:NGFiNTZmNWJkNjVhNDhkNGJmYmI0Yjg5NmI0ZTM5ZGI=|2e0b8b7c1103b867db15188dcdbfbc6126c845d412a8ef84b57b59dd2ee04fc7"; z_c0="2|1:0|10:1585189717|4:z_c0|92:Mi4xYVNpN0FnQUFBQUFBa09OVExrOGREeVlBQUFCZ0FsVk5WV0ZwWHdDelozbjIxX19WSjNXNWZLNDNrQ29yd0NsRGxn|ccb6f7fa59996f6e94b47479e0438da237bbc9d88372d13c66233f4cc169616e"; _gat_gtag_UA_149949619_1=1; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585203777; KLBRSID=ca494ee5d16b14b649673c122ff27291|1585203778|1585203773'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

for cookie in cookies.split(";"):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
print(r.text)

























