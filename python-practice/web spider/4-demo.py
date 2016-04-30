# -*- coding: utf-8 -*-

import urllib2
import re
import thread
import time

# ----------- 加载处理糗事百科 -----------


class SpiderModel:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    # 将所有的段子都扣出来，添加到列表中并且返回列表
    def getpage(self, page):

        print("正在加载中请稍候......")
        my_url = "http://www.qiushibaike.com/8hr/page/" + page
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' \
                     '50.0.2661.86 Safari/537.36'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(my_url, headers=headers)
        my_response = urllib2.urlopen(req)
        my_page = my_response.read()
        unicode_page = my_page
        my_items = re.findall('<div.*?class="content">(.*?)</div>', unicode_page, re.S)
        items = []
        for item in my_items:
            items.append(item.replace("<br/>", "\n"))
        return items

    # 加载新的页面
    def load_page(self):
        while self.enable:
            # 如果pages数组中的内容小于2个
            if len(self.pages) < 2:
                try:
                    # 获取新的页面中的段子们
                    my_page = self.getpage(str(self.page))
                    self.page += 1
                    self.pages.append(my_page)
                except Exception as e:
                    print 'except:', e
                    print '无法链接糗事百科！\n'
            else:
                time.sleep(1)

    def show_page(self, now_page, page):
        for items in now_page:
            print u'\n 第%d页, 第%d题:' % (page, now_page.index(items) + 1), items
            my_input = raw_input('回车浏览下一个:')
            if my_input == "quit":
                self.enable = False
                break

    def start(self):
        self.enable = True
        page = self.page

        # 新建一个线程在后台加载段子并存储
        thread.start_new_thread(self.load_page, ())

        # ----------- 加载处理糗事百科 -----------
        while self.enable:
            # 如果self的page数组中存有元素
            if self.pages:
                now_page = self.pages[0]
                del self.pages[0]
                self.show_page(now_page, page)
                page += 1


# ----------- 程序的入口处 -----------
print u"""
---------------------------------------
   程序：糗百爬虫
   版本：0.3
   作者：why
   日期：2014-06-03
   语言：Python 2.7
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
   原文地址(源代码):http://blog.csdn.net/pleasecallmewhy/article/details/8932310
   修改内容:网址和正则表达式部分
   修改者:Ryan
   修改日期:2015-09-19
   测试通过版本:Python 2.7.10
---------------------------------------
"""
myModel = SpiderModel()
myModel.start()
