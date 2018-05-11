# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from openpyxl import Workbook


class AutohomeExcelPipeline(object):

    def __init__(self):
        # 创建Excel
        self.wb = Workbook()
        # 激活Excel
        self.ws = self.wb.active
        self.ws.append(['类型', u'标题', u'发布者昵称', u'发布图片', u'本地路径', u'发布时间'])  # 设置表头

    def process_item(self, item, spider):
        line = [item['tag'], item['title'], item['user'], item['url'], item['local_url'], item['push_time']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        return item

    def close_spider(self, spider):
        self.wb.save(u'autohomeSpider.xlsx')  # 保存xlsx文件
