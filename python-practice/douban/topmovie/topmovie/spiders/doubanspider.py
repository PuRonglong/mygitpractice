# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from topmovie.items import TopmovieItem


class Douban(CrawlSpider):
    name = 'douban'
    redis_key = 'douban:start_urls'
    start_urls = ['https://movie.douban.com/top250']
    url = 'https://movie.douban.com/top250'

    def parse(self, response):
        item = TopmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each

            MovieInfo = eachMovie.xpath('div[@class="bd"/p/text()]').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            # quote可能为空,进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''

            item['title'] = fullTitle
            item['movieInfo'] = '/'.join(MovieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item

        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(self.url + nextLink, callback=self.parse)
