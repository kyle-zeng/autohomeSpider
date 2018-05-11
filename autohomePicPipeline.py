# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib


class AutohomePicPipeline(object):


    def process_item(self, item, spider):
        filename = u'{}_{}.jpg'.format(item['user'], item['title'])
        tag = item['tag']
        img_path = u'F:/python/pic/{}'.format(tag)

        if not os.path.exists(img_path):
            os.makedirs(img_path)
            print
            img_path + u' 创建成功'
        img_url = "http:{}".format(item['url'])
        with open(img_path + '/' + filename, 'wb') as f:
            f.write(urllib.request.urlopen(img_url).read())
        item['local_url'] = img_path + '/' + filename
        return item
