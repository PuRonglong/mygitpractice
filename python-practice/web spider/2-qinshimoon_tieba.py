# -*- coding: utf-8 -*-

import string, urllib2


def qinshi_tieba(url, page_begin, page_end):
	for i in range(page_begin, page_end + 1):
		sName = string.zfill(i, 5) + '.html'
		print '正在下载第' + str(i) + '页，并存储为' + sName + '...'
		f = open(sName, 'w+')
		m = urllib2.urlopen(url + str(i)).read()
		f.write(m)
		f.close()


# url = 'http://tieba.baidu.com/p/4510793112?pn='

url = str(raw_input('输入贴吧地址：'))

page_begin = int(raw_input('请输入开始页：'))

page_end = int(raw_input('结束页：'))

qinshi_tieba(url, page_begin, page_end)