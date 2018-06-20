# -*- coding: utf-8 -*-
import scrapy
from mingyan.items import MingyanItem
import telnetlib


class xuaiSpaider(scrapy.Spider):
    name = "ipdaili"    #爬虫名称
    star_urls=('https://www.kuaidaili.com/')    #爬虫网页地址

    def start_requests(self):   #定义函数，要爬取得多个页面
        reqs=[]

        for i in range(1,5):
            req=scrapy.Request("https://www.kuaidaili.com/free/inha/%s/"%i)
            reqs.append(req)

        return reqs

    def parse(self, response):  #对爬取得网页进行分析，提取想要的部分
        ip_list=response.xpath('//*[@id="list"]/table/tbody')
        trs=ip_list[0].xpath('tr')
        items=[]

        for ip in trs[0:]:      #使用xpath选择器来选取我们想要的网页标签内容
            pre_item=MingyanItem()

            pre_item['IP']=ip.xpath('td[1]/text()').extract()
            pre_item['PORT'] = ip.xpath('td[2]/text()').extract()
            pre_item['ANONYMOUS'] = ip.xpath('td[3]/text()').extract()
            pre_item['TYPE'] = ip.xpath('td[4]/text()').extract()
            pre_item['DNS_POSITION'] = ip.xpath('td[5]/text()').extract()
            pre_item['SPEED'] = ip.xpath('td[6]/text()').extract()
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[7]/text()').extract()
            items.append(pre_item)

            # if self.telnet(pre_item):   #ip
            #     items.append(pre_item)

        return items




    # def telnet(self,pre_item): #判断是否有效
    #     try:
    #         telnetlib.Telnet(pre_item['IP'],port=pre_item['PORT'],timeout=10.0)
    #     except:
    #         print('connect failure')
    #         return False
    #     else:
    #         print('connect success')
    #         return True

