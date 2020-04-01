# -*- coding: UTF-8 -*-
from lxml import etree

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

html = etree.parse('data/test.html', etree.HTMLParser())
# result = html.xpath('//li')
# print(result)
# print(result[0])
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)
# result = html.xpath('//li[@class="item-0"]')
# print(result)
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)
result = html.xpath('//li/a/@href')
print(result)

























