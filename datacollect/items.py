# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DatacollectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cat = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    answer = scrapy.Field()
    source = scrapy.Field()
    pass