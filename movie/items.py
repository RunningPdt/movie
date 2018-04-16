# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()       #电影名称
    movieInfo = scrapy.Field()   #电影信息
    star = scrapy.Field()        #豆瓣评分
    quote = scrapy.Field()       #电影概括
    pass
