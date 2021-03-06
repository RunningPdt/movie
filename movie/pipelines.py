# encoding:utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MoviePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Hc520Wby', db='huangchong')
        self.cursor = self.conn.cursor()
        # self.cursor.execute("truncate table movie")  # 清空表数据
        # self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into movie (title, movie_info, star, quote) VALUES ('{}', '{}', '{}', '{}');".
                                format(item['title'], item['movie_info'], item['star'], item['quote']))
            self.conn.commit()
        except pymysql.Error:
            print("Error'{}','{}','{}','{}'".format(item['title'], item['movie_info'], item['star'], item['quote']))
        return item
