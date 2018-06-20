# IPdaili
爬取ip代理网站
爬取https://www.kuaidaili.com/网站

字段信息：
    IP=scrapy.Field()       #爬取代理ip
    PORT=scrapy.Field()     #爬取端口
    ANONYMOUS=scrapy.Field()    #匿名度
    TYPE=scrapy.Field()     #类型
    DNS_POSITION=scrapy.Field()  #位置
    SPEED=scrapy.Field()    #响应速度
    LAST_CHECK_TIME=scrapy.Field()  #最后验证时间
	
爬取字段保存到mysql数据库
数据库连接配置在settings中
	
	
