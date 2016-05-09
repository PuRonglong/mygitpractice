# -*- coding: utf-8 -*-
# 豆瓣电影top250排行榜爬虫

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from topmovie.items import TopmovieItem


class Douban(CrawlSpider):
    name = 'topmovie'
    redis_key = 'topmovie:start_urls'
    start_urls = ['http://movie.douban.com/top250']
    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = TopmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each

            MovieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            # quote可能为空,进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''

            item['title'] = fullTitle
            item['movieInfo'] = MovieInfo[0] + '\n' + MovieInfo[1]
            item['star'] = star
            item['quote'] = quote
            yield item

        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(self.url + nextLink, callback=self.parse)
