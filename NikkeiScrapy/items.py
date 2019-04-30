# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NikkeiItem(scrapy.Item):
    I1_title = scrapy.Field()
    I2_detail = scrapy.Field()
    I3_insert_datetime = scrapy.Field()
    pass