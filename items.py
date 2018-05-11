# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 图片链接地址
    url = scrapy.Field()
    # 发布者
    user = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    # 本地存储路径
    local_url = scrapy.Field()
    # 发布时间
    push_time = scrapy.Field()
    # 图片ID
    pic_id = scrapy.Field()
    pass
