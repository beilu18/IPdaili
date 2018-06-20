# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MingyanPipeline(object):
    def process_item(self, item, spider):
        #连接数据库


        DBKWARGS = spider.settings.get('DBKWARGS')
        conn = pymysql.connect(**DBKWARGS)

        #创建游标
        cur=conn.cursor()

        #插入数据
        sql=("INSERT INTO IPdaili(IP,PORT,ANONYMOUS,TYPE,DNS_POSITION,SPEED,LAST_CHECK_TIME) VALUES (%s,%s,%s,%s,%s,%s,%s)")

        lis=(item['IP'],item['PORT'],item['ANONYMOUS'],item['TYPE'],item['DNS_POSITION'],item['SPEED'],item['LAST_CHECK_TIME'])

        try:
            cur.execute(sql,lis)
        except Exception as e:
            print("insert errot",e)
            conn.rollback()     #错误回滚
        else:
            conn.commit()       #提交sql

        cur.close()

        conn.close()        #关闭连接

        return item
