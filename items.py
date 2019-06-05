# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WDYPipeline(scrapy.Item):
    href=scrapy.Field()
    src=scrapy.Field()
    title=scrapy.Field()
    label=scrapy.Field()
    up_num=scrapy.Field()
