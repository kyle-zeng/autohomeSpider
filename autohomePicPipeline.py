# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib


class AutohomePicPipeline(object):

    def process_item(self, item, spider):
        # 图片保存名称
        filename = u'{}_{}.jpg'.format(item['user'], item['title'].strip())
        # 图片保存路径
        img_path = u'F:/python/pic/{}'.format(item['tag'])

        if not os.path.exists(img_path):
            os.makedirs(img_path)
            print
            img_path + u' 创建成功'

        img_url = "http:{}".format(item['url'])
        with open(img_path + '/' + filename, 'wb') as f:
            f.write(urllib.request.urlopen(img_url).read())
        # 保存本地路径，写入Excel用
        item['local_url'] = img_path + '/' + filename
        return item
