# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = MovieItem()
        for sel in response.xpath('//div[@class="info"]'):
            title = sel.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = sel.xpath('div[@class="bd"]/p/text()').extract()
            star = sel.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = sel.xpath('div[@class="bd"]/p/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo).replace(' ', '').replace('\n', '')
            item['star'] = star[0]
            item['quote'] = quote
            yield item
        nextPage = response.xpath('//span[@class="next"]/link/@href').extract()
        if nextPage:
            nextPage = nextPage[0]
            print(self.start_urls[0] + str(nextPage))
            yield scrapy.Request(self.start_urls[0] + str(nextPage), callback=self.parse)
