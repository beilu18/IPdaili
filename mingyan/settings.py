# -*- coding: utf-8 -*-

# Scrapy settings for mingyan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mingyan'  #scrapy项目的名字，自动被赋值

SPIDER_MODULES = ['mingyan.spiders']
NEWSPIDER_MODULE = 'mingyan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mingyan (+http://www.yourdomain.com)'    #爬取默认
USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3      #下载器在下载同一个网站下一个页面前需要等待的时间,该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单位
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16    #对单个网站进行并发请求的最大值。
#CONCURRENT_REQUESTS_PER_IP = 16        # 对单个IP进行并发请求的最大值。如果非0,则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。
                                        # 也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。

#禁用Cookie（默认情况下启用）
# Disable cookies (enabled by default)
COOKIES_ENABLED = False


#禁用Telnet控制台（默认启用）
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


#覆盖默认请求标头：
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}


#启用或禁用蜘蛛中间件
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mingyan.middlewares.MingyanSpiderMiddleware': 543,
#}


#启用或禁用下载器中间件
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'mingyan.middlewares.MingyanDownloaderMiddleware': 543,
#}


#启用或禁用扩展程序
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


#配置项目管道
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'mingyan.pipelines.MingyanPipeline': 300,
}
LOG_FILE = "scrapy.log"


#启用和配置AutoThrottle扩展（默认情况下禁用）
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True

#初始下载延迟
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5

#在高延迟的情况下设置的最大下载延迟
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60

#Scrapy请求的平均数量应该并行发送每个远程服务器
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

#启用显示所收到的每个响应的调节统计信息：
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False


#启用和配置HTTP缓存（默认情况下禁用）
# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#数据库连接配置
DBKWARGS = {'db':'Crawler','user':'root','passwd':'123456',
            'host':'localhost','use_unicode':True,'charset':'utf8'}

