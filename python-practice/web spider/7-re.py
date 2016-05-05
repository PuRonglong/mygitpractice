# -*- coding: utf-8 -*-

import requests
import urllib
import re
import time
import random


def main():
    url = 'https://www.zhihu.com/question/31159026/followers'
    headers = {
        # 'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        '50.0.2661.86 Safari/537.36',
        # 'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
        # "Connection": "close",
        # 'Accept - Encoding': 'gzip, deflate, sdch',
        # 'Accept - Language': 'zh - CN, zh;q = 0.8, en;q = 0.6, zh - TW;q = 0.4',
        # 'Cache - Control': 'no - cache',
        # 'Upgrade - Insecure - Requests': '1'
    }

    i = 1
    for x in xrange(20, 100, 20):
        data = {
            'start': '0',
            'offset': str(x),
            '_xsrf': '6808df9a2c86d04be2a76eae611e486c'
        }

        content = requests.post(url, headers=headers, data=data, timeout=10).text

        # 在爬下来的json上用正则提取图片地址,去掉_m为大图
        imgs = re.findall('<img src=\\\\\"(.*?)_m.jpg', content)

        for img in imgs:
            try:
                img = img.replace('\\', '')
                pic = img + '.jpg'
                path = 'Users/puronglong/Desktop' + str(i) + '.jpg'

                # 存储
                urllib.urlretrieve(pic, path)

                print '下载了第%d张图' % str(i)
                i += 1

                # 睡眠函数防止爬取过快被封
                time.sleep(random.uniform(0.5, 1))

            except:
                print '抓漏1张'
                pass
                time.sleep(random.uniform(0.5, 1))

main()
