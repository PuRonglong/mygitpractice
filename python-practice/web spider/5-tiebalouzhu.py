# -*- coding: utf-8 -*-

import urllib2
import re


class ShiJianTianXia:

    # 声明相关属性
    def __init__(self, url):
        self.url = (url + 'see_lz=1')
        # self.url = url + '?see_lz=1'
        self.page = 1
        self.datas = []

    # 找出当前页的帖子
    def find_page(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' \
                     '50.0.2661.86 Safari/537.36'
        headers = {'User-Agent': user_agent}
        my_req = urllib2.Request(self.url, headers=headers)
        print self.url
        current_page = urllib2.urlopen(my_req).read().decode('utf-8')

        # 找出当前页总页数
        last_page = self.find_count(current_page)

        # 找到标题
        post_title = self.find_title(current_page)
        print '帖子主题:', post_title

        # 保存数据
        self.txt_data(self.url, post_title, last_page)

    # 找出当前页总页数
    def find_count(self, current_page):
        my_match = re.search('<span.*class="red">(\d\d)</span>', current_page, re.S)

        if my_match:
            last_page = int(my_match.group(1))
            print "总帖子数:%d" % last_page
        else:
            last_page = 0
            print '未找到帖子总数'

        return last_page

    # 找到标题
    def find_title(self, current_page):
        my_match = re.search('<h3.*?>(.*?)</h3>', current_page, re.S)
        post_title = '暂无标题'

        if my_match:
            post_title = my_match.group(1)
        else:
            print '未找到标题'

        post_title = post_title.replace('\\', '').replace('/', '').replace('*', '').replace('?', '').replace('"', '').\
            replace('>', '').replace('...', '')
        return post_title

    # 将获取的帖子内容另存为
    def txt_data(self, url, post_title, last_page):

        # 获取所有帖子
        self.save_data(url, last_page)

        # 建立本地文件并存储内容
        f = open(post_title + '.txt', 'w+')
        f.writelines(self.datas)
        f.close()

        print '已将上面内容全部下载到本地并存储为txt文件;'
        print '按回车键退出...'
        raw_input()

    # 获取这个主题后面的页
    def save_data(self, url, last_page):
        url = url + '&pn='
        for i in range(1, last_page + 1):
            print '正在下载第%d页内容;' % i
            # 读取第i页内容
            current_page = urllib2.urlopen(url + str(i)).read().decode('utf-8')
            # 将第i页内容从页面中取出并存储
            self.get_data(current_page)

    # 将帖子内容从页面中取出并存储
    def get_data(self, current_page):
        my_posts = re.findall('<div.*?class="d_post_content j_d_post_content ">(.*?)</div>', current_page, re.S)
        for my_post in my_posts:
            data = my_post.replace('<br>', '\n').encode('utf-8')
            self.datas.append(data)

print "输入贴吧地址:"
input_url = str(raw_input(''))
louzhu = ShiJianTianXia(input_url)
louzhu.find_page()
