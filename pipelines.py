# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WdyPipeline(object):

    def open_spider(self,spider):
        self.connect=pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123123',
            db='weidianying',
            charset='utf8'
        )
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        print(item['label'])
        insert_sql="INSERT INTO app01_movie(label,href,up_num,src,title)VALUES(%s,%s,%s,%s,%s)"
        self.cursor.execute(insert_sql,(item['label'],item['href'],item['up_num'],item['src'],item['title']))
        self.connect.commit()
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
