# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from yandeCrawl import settings

class YandecrawlPipeline(object):

    def __init__(self):
        self.images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        # 创建目录
        if not os.path.exists(self.images_path):
            os.mkdir(self.images_path)

    def process_item(self, item, spider):
        # file_name = item('file_name')
        img_urls = item('images_urls')
        for url in img_urls:
            image_name = str(url).split('_')[-1]
            request.urlretrieve(url, os.path.join(self.images_path, image_name))
        return item


class YandecrawlImagesPipeline(ImagesPipeline):
    # 在发送下载请求之前调用,本身就是发送下载请求的
    def get_media_requests(self, item, info):
        request_objs = super(YandecrawlImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    # 图片将要被存储时调用,获取图片存储路径
    def file_path(self, request, response=None, info=None):
        path = super(YandecrawlImagesPipeline, self).file_path(request, response, info)
        category = request.item.get('category')
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace('full/', '')
        image_path = os.path.join(category_path, image_name)
        return image_path
