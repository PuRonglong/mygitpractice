# -*- coding: utf-8 -*-

import urllib2
import re
import time
import thread


class QiuShiBaiKe:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    # 获取当前page的段子
    def get_page(self, page):

        my_url = 'http://www.qiushibaike.com/8hr/page/' + page
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' \
                     '50.0.2661.86 Safari/537.36'
        headers = {'User-Agent': user_agent}
        my_req = urllib2.Request(my_url, headers=headers)
        my_res = urllib2.urlopen(my_req)
        my_page = my_res.read()

        my_items = re.findall('<div.*?class="content">(.*?)</div>', my_page, re.S)

        items = []
        for my_item in my_items:
            items.append(my_item.replace('<br>', '\n'))

        # items中存储当前页的所有段子
        return items

    # 操作当前page并将self.page+1
    def next_page(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    my_page = self.get_page(str(self.page))
                    self.page += 1
                    self.pages.append(my_page)

                except Exception as e:
                    print 'except:', e
                    print '无法链接糗事百科！\n'
            else:
                time.sleep(1)

    # 显示当前页detail
    def show_page(self, now_page_detail, page):

        for item in now_page_detail:
            print "第%d页, 第%d题:" % (page, now_page_detail.index(item) + 1), item
            my_input = raw_input('回车浏览下一个:')
            if my_input == 'quit':
                self.enable = False
                break

    def start(self):
        self.enable = True
        page = self.page

        # 新建一个线程在后台加载段子并存储
        thread.start_new_thread(self.next_page, ())

        while self.enable:
            if self.pages:
                now_page_detail = self.pages[0]
                del self.pages[0]
                self.show_page(now_page_detail, page)
                page += 1

print u'''
    开始获取糗事百科段子:
'''

myModel = QiuShiBaiKe()
myModel.start()
