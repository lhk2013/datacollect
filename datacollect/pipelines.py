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

            count_answer = self.find_by_answer(item)
            count_question = self.find_by_title(item)

            if count_answer <= 0 and count_question<=0:
                self.save_subject(item)

            else:
                print "已经保存过该答案"


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

    def find_by_answer(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = ' SELECT %s FROM t_spider_collect  WHERE answer=%s' % (fields, "%s")
        print sql
        print values
        cursor.execute(sql, item["answer"])
        result = cursor.fetchall()
        db.connection.commit()
        return result.__len__()

    def find_by_title(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = ' SELECT %s FROM t_spider_collect  WHERE title=%s' % (fields, "%s")
        print sql
        print values
        cursor.execute(sql, item["title"])
        result = cursor.fetchall()
        db.connection.commit()
        return result.__len__()