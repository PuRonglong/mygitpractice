# -*- coding: utf-8 -*-

import requests
import re


class JiKeXueYuan:

    def __init__(self):
        print u'开始爬取内容...'

    # 获取网页url
    def get_url(self, url, total_page):
        page_group = []  # 存储所有要爬的页

        now_page = re.search('pageNum=(\d+)', url, re.S).group(1)
        for i in (now_page, total_page):
            each_link = re.sub('pageNum=\d+', 'pageNum=%s' % i, url, re.S)
            page_group.append(each_link)

        return page_group

    # 获取网页源代码
    def get_soucre(self, url):
        html = requests.get(url)
        text = html.text
        return text

    # 获取一页里的课程
    def get_course(self, html):
        course = re.findall('<li id=.*?</li>', html, re.S)
        return course

    # 获取一门课程的信息
    def get_course_info(self, one_course):
        one_course_info = {}

        one_course_info['title'] = re.search('alt="(.*?)">', one_course, re.S).group(1)
        time_and_level = re.findall('<em>(.*?)</em>', one_course, re.S)
        number = time_and_level[0].split()
        one_course_info['time'] = number[0] + ' ' + number[1]
        one_course_info['level'] = time_and_level[1]
        content = re.search('display: none;">(.*?)</p>', one_course, re.S).group(1)
        one_course_info['content'] = content.split()[0]
        one_course_info['people'] = re.search('<em class="learn-number">(.*?)</em>', one_course, re.S).group(1)

        return one_course_info

    # 存储课程信息
    def save_course_info(self, course_info):
        f = open('info.txt', 'w+')

        for each_course in course_info:
            f.write('title:' + each_course['title'].encode("utf-8") + '\n')
            f.write('content:' + each_course['content'].encode("utf-8") + '\n')
            f.write('time:' + each_course['time'].encode("utf-8") + '\n')
            f.write('people:' + each_course['people'].encode("utf-8") + '\n')
            f.write('level:' + each_course['level'].encode("utf-8") + '\n')

        f.close()

if __name__ == '__main__':  # 如果程序是自己使用.py文件运行

    class_info = []  # 存储课程信息
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'

    jikexueyuan = JiKeXueYuan()
    all_links = jikexueyuan.get_url(url, 2)
    for each_link in all_links:

        # 获取一页的源代码
        html = jikexueyuan.get_soucre(each_link)

        # 获取一页的所有课程
        page_course = jikexueyuan.get_course(html)

        for one_course in page_course:

            # 获取一门课程的详细信息
            one_course_info = jikexueyuan.get_course_info(one_course)

            # 存储一门课程的详细信息
            class_info.append(one_course_info)

    jikexueyuan.save_course_info(class_info)
