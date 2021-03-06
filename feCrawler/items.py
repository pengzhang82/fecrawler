# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    ytd = scrapy.Field()
    one_yr = scrapy.Field()
    three_yr = scrapy.Field()
    five_yr = scrapy.Field()


class TypecodecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    isin = scrapy.Field()
    typecode = scrapy.Field()
   
