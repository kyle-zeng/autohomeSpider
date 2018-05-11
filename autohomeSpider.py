
import scrapy
from lxml import etree
from autohomeSpider.items import AutohomespiderItem

class autohomeSpider(scrapy.Spider):
    name = "autohomeSpider"
    allowed_domains = ["autohome.com.cn"]
    base_url = u'https://club.autohome.com.cn/JingXuan/104/{}'
    page = 1
    start_urls = [
        base_url.format(page)
    ]

    def parse(self, response):
        # 解析
        datas = response.xpath('//div[@class="choise-con"]/ul[@class="content"]/li')
        for data in datas:
            title = data.xpath('.//div[@class="pic-box"]/a/@title').extract()[0]
            url = data.xpath('.//div[@class="pic-box"]/a/img/@data-original').extract()[0]
            tag = data.xpath('.//div[@class="pic_txt"]/span[@class="model-num"]/text()').extract()[0]
            user = data.xpath('.//div[@class="pic_txt"]/dl/dt[@class="user"]/a/span/text()').extract()[0]
            item = AutohomespiderItem(title = title, url = url, tag = tag, user = user)
            yield item

        self.page = self.page+1
        next_href = self.base_url.format(self.page)
        next_page = response.urljoin(next_href)
        # 回调parse处理下一页的url
        print("处理下一页：" +  next_href)
        if(self.page < 10):
            yield scrapy.Request(next_page, callback=self.parse)
