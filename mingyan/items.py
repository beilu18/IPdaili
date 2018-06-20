# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MingyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass

    IP=scrapy.Field()       #爬取代理ip
    PORT=scrapy.Field()     #爬取端口
    ANONYMOUS=scrapy.Field()    #匿名度
    TYPE=scrapy.Field()     #类型
    DNS_POSITION=scrapy.Field()  #位置
    SPEED=scrapy.Field()    #响应速度
    LAST_CHECK_TIME=scrapy.Field()  #最后验证时间
