# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yandeCrawl.items import YandecrawlItem


class MengmeiSpider(CrawlSpider):
    name = 'mengmei'
    # 爬取y站
    # allowed_domains = ['yande.re', 'files.yande.re']
    # start_urls = ['https://yande.re/post']
    # 爬取k站
    allowed_domains = ['konachan.com']
    start_urls = ['http://konachan.com/post']

    rules = (
        Rule(LinkExtractor(allow=r'/post\?page=+\d'), callback='parse_page', follow=True),
        # Rule(LinkExtractor(allow=r'/post/show/+\d'), callback='parse_item', follow=False),
    )

    def parse_page(self, response):
        category = 'dongman'
        view_urls = response.xpath('//div/ul[@id="post-list-posts"]/li')
        for url in view_urls:
            image_url = url.xpath('./a/@href').extract()
            # print(image_url)
            yield YandecrawlItem(image_urls=image_url, category=category)


