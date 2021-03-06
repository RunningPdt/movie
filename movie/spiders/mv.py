# encoding:utf-8
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
            full_title = ''
            for each in title:
                full_title += each
            movie_info = sel.xpath('div[@class="bd"]/p/text()').extract()
            star = sel.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = sel.xpath('div[@class="bd"]/p/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = full_title
            print(item['title'].encode('GBK', 'ignore').decode('GBK'))
            item['movie_info'] = ';'.join(movie_info).replace(' ', '').replace('\n', '')
            print(item['movie_info'].encode('GBK', 'ignore').decode('GBK'))
            item['star'] = star[0]
            print(item['star'])
            item['quote'] = quote
            print(item['quote'].encode('GBK', 'ignore').decode('GBK'))
            yield item
        next_page = response.xpath('//span[@class="next"]/link/@href').extract()
        if next_page:
            next_page = next_page[0]
            print(self.start_urls[0] + str(next_page))
            yield scrapy.Request(self.start_urls[0] + str(next_page), callback=self.parse)
