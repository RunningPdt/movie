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
            print(title)
            full_title = ''
            for each in title:
                full_title += each
            movie_info = sel.xpath('div[@class="bd"]/p/text()').extract()
            print(movie_info)
            star = sel.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            print(star)
            quote = sel.xpath('div[@class="bd"]/p/span/text()').extract()
            print(quote)
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = full_title.replace(u'\xa0', u'')
            item['movie_info'] = ';'.join(movie_info).replace(' ', '').replace('\n', '').replace(u'\xa0', u'')
            item['star'] = star[0].replace(u'\xa0', u'')
            item['quote'] = quote.replace(u'\xa0', u'')
            yield item
        next_page = response.xpath('//span[@class="next"]/link/@href').extract()
        if next_page:
            next_page = next_page[0]
            print(self.start_urls[0] + str(next_page))
            yield scrapy.Request(self.start_urls[0] + str(next_page), callback=self.parse)
