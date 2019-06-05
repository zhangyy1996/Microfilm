# -*- coding: utf-8 -*-
import scrapy
from WDY.items import WDYPipeline

class WdySpider(scrapy.Spider):
    name = 'wdy'
    allowed_domains = ['www.vmovier.com']
    start_urls = ['http://www.vmovier.com/']

    def start_requests(self):
        url='https://www.vmovier.com/'
        yield scrapy.Request(url,callback=self.index_page,dont_filter=False,)
    def index_page(self,response):
        srcs=response.xpath('//*[@id="post-list"]/li/a/img/@src').extract()
        titles=response.xpath('//*[@id="post-list"]/li/div/h1/a/text()').extract()
        labels=response.xpath('//*[@id="post-list"]/li/div/div[2]/a/text()').extract()
        hrefs=response.xpath('//*[@id="post-list"]/li/a/@href').extract()
        up_nums=response.xpath('//*[@id="post-list"]/li/div/div[3]/span[2]/text()').extract()
        z=[t for t in zip(srcs,titles,labels,hrefs,up_nums)]
        for i in z:
            item = WDYPipeline()
            item['src']=i[0]
            item['title']=i[1]
            item['label']=i[2]
            item['href']='https://www.vmovier.com'+i[3]
            item['up_num']=i[4].strip()

            yield item

