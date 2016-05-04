# -*- coding: utf-8 -*-
# urllib.urlretrieve()直接下载数据

import urllib


path = '1.png'
url = 'https://img3.doubanio.com/view/photo/photo/public/p480747492.jpg'

urllib.urlretrieve(url, path)
