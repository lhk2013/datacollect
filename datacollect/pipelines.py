# -*- coding: utf-8 -*-
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datacollect.database as db
cursor = db.connection.cursor()



class DatacollectPipeline(object):
    # 初始化的操作，这里我们做本地化直接写成文件，所以初始化文件对象
    def __init__(self):
        print('实例化DatacollectPipeline')
        # self.f = open('itcast_pipeline.json', 'w')


    def process_item(self, item, spider):

        if item != None:

            self.save_subject(item)

            # '''
            # subject
            # '''
            # exist = self.get_subject(item)
            # if not exist:
            #     self.save_subject(item)



    #结束后做的操作，在这里我们要关闭文件
    def close_spider(self,spider):
        print('结束')
        # self.f.close()


    def save_subject(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO t_spider_collect (%s) VALUES (%s)' % (fields, temp)
        print sql
        print values
        cursor.execute(sql, values)
        return db.connection.commit()
