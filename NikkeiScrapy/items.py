# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NikkeiItem(scrapy.Item):
    title = scrapy.Field()
    detail = scrapy.Field()
    insert_datetime = scrapy.Field()
    pass