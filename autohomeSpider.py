
import scrapy
import time
from autohomeSpider.items import AutohomespiderItem


class autohomeSpider(scrapy.Spider):

    name = "autohomeSpider"
    allowed_domains = ["autohome.com.cn"]
    # url地址
    base_url = u'https://club.autohome.com.cn/JingXuan/104/{}'
    # 页码
    page = 1
    start_urls = [
        base_url.format(page)
    ]

    def __init__(self):
        self.title = ''
        #self.url = ''
        self.tag = ''
        self.user = ''
        #self.href = ''

    def parse(self, response):
        # 解析
        datas = response.xpath('//div[@class="choise-con"]/ul[@class="content"]/li')
        for data in datas:
            self.title = data.xpath('.//div[@class="pic-box"]/a/@title').extract()[0]
            #self.url = data.xpath('.//div[@class="pic-box"]/a/img/@data-original').extract()[0]
            self.tag = data.xpath('.//div[@class="pic_txt"]/span[@class="model-num"]/text()').extract()[0]
            self.user = data.xpath('.//div[@class="pic_txt"]/dl/dt[@class="user"]/a/span/text()').extract()[0]

            href = data.xpath('.//div[@class="pic-box"]/a/@href').extract()[0]
            # item = AutohomespiderItem(title = self.title, url = self.url, tag = self.tag, user = self.user)
            # yield item
            href = u'http:{}'.format(href)
            time.sleep(1)
            yield scrapy.Request(href, callback=self.parse_detail)

        self.page = self.page+1
        next_href = self.base_url.format(self.page)
        next_page = response.urljoin(next_href)
        # 回调parse处理下一页的url
        print("处理下一页：" + next_href)
        if(self.page < 10):
            time.sleep(1)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):
        # 解析
        push_time = response.xpath('//div[@class="plr26 rtopcon"]/span[xname="date"]').extract()[0]
        details = response.xpath('//div[@class="conttxt"]/div[@class="w740"]/div[@class="tz-figure"]')
        for detail in details:
            url = detail.xpath('.//div[@class="x-loaded"]/img/@src').extract()[0]
            pic_id = detail.xpath('.//div[@class="x-loaded"]/img/@id').extract()[0]
            item = AutohomespiderItem(title=self.title, url=url, tag=self.tag, user=self.user, push_time=push_time, pic_id=pic_id)
            yield item