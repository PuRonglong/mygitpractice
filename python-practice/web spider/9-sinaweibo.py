# -*- coding: utf-8 -*-


import requests
from lxml import etree
from multiprocessing.dummy import Pool

cook = {'Cookie': 'SUB=_2A256NYzHDeRxGeVM7VEW9y3NwzyIHXVZ2RSPrDV6PUJbrdANLUL4kW1LHetVkHay;'
                    # 'SUHB=0S7CmQDvF5sFOA;'
                    'gsid_CTandWM=4uY1b01b15aEHJbF6EIFldH3v2U;'
                     '_T_WM=5c439bc8faa04fb670e1c484321c6f1a;'}

url = 'http://weibo.cn/u/3263773180'
html = requests.get(url, cookies=cook).content
selector = etree.HTML(html)

# selector = Selector(html)
post = selector.xpath('//span[@class="ctt"]')

for each in post:
    text = each.xpath('string(.)')
    print text
