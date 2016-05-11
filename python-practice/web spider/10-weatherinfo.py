# -*- coding: utf-8 -*-

import requests
import xlwt
from bs4 import BeautifulSoup


def get_html():
    global h
    s = requests.session()
    url = 'http://www.whepb.gov.cn/airSubair_water_lake_infoView/v_listhistroy.jspx?type=0'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
        'Referer':'http://www.whepb.gov.cn/airSubair_water_lake_infoView/v_listhistroy.jspx?type=0',
        'Host':'www.whepb.gov.cn',
        'Cookie':'JSESSIONID=C20EA30BE656FA09F12E044D8180A1DC.tomcat; JSESSIONID=C20EA30BE656FA09F12E044D8180A1DC.tomcat; JSESSIONID=C20EA30BE656FA09F12E044D8180A1DC.tomcat; clientlanguage=zh_CN',
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Accept-Encoding':'gzip, deflate',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    data = {
        'pageNo1': '1',
        'pageNo2': '',
        'cdateEnd': ''
    }

    html = s.post(url, headers=headers, data=data).content
    h = html.decode('utf-8')


def get_excel():
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = workbook.add_sheet('data', cell_overwrite_ok=True)
    get_html()
    i = 0
    soup = BeautifulSoup(h, 'lxml')

    for eachtr in soup.find_all('tr'):
        j = 0
        for eachtd in eachtr.find_all('td'):
            sheet.write(i, j, eachtd.get_text())
            j += 1
        i += 1

    workbook.save('10-weatherinfo.xls')

get_excel()
