# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import thread
import time

class qiushibaike:

	def __init__(self):
		self.page = 1
		self.pages = []
		self.enable = true

	def getArticle(self, article):
		url = "http://www.qiushibaike.com/article/" + article
		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'
		headers = {'User-agent' : user_agent}
		myReq = urllib2.Request(url, headers = headers)
		myRes = urllib2.urlopen(req)
		myArticle = myRes.read()

		unicodeArticle = myArticle.decode('utf-8')

		#找出当前页面中class为content的div段
		myItems = re.findall('<div.*?class="content">(.*?)</div>',unicodePage,re.S)