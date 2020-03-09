# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YandecrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
    # file_name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    # images = scrapy.Field()

