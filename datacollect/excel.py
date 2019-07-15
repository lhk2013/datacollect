# -*- coding: utf-8 -*-

import xlwt
import datacollect.database as db
from datetime import datetime

import sys

reload(sys)

sys.setdefaultencoding('utf-8')

cursor = db.connection.cursor()

def export_excel(name, data):

    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
    today = datetime.today()
    # 将获取到的datetime对象仅取日期如：2016-8-9
    today_date = datetime.date(today)
    # 遍历result中的没个元素。
    for i in xrange(len(result)):
        # 对result的每个子元素作遍历，
        for j in xrange(len(result[i])):
            # 将每一行的每个元素按行号i,列号j,写入到excel中。
            sheet.write(i, j, result[i].values().__getitem__(j))
    # 以传递的name+当前日期作为excel名称保存。
    wbk.save(name + str(today_date) + '.xls')


def export_txt(name, data):




    today = datetime.today()
    # 将获取到的datetime对象仅取日期如：2016-8-9
    today_date = datetime.date(today)
    # 遍历result中的没个元素。
    with open(name+".txt", "w+") as f:
        for i in xrange(len(result)):
            # 对result的每个子元素作遍历，
            f.write("Question:"+result[i]["title"] + "\rAnswer:" + result[i]["answer"] + "\r\n")

            # for j in xrange(len(result[i])):
            #     # 将每一行的每个元素按行号i,列号j,写入到excel中。
            #     prefix = ""
            #     if j %2 == 1:
            #         prefix = "Question:"
            #     else:
            #         prefix = "Answer"
            #     f.write(result[i].keys().__getitem__(j)+":"+result[i].values().__getitem__(j).decode("utf-8")+"\r")
            # f.write("\n")


if __name__ == '__main__':

    sql = ' SELECT title,answer FROM t_spider_collect  WHERE cat=%s AND CHAR_LENGTH(answer)>20 and CHAR_LENGTH(answer)<300 AND CHAR_LENGTH(title) >4'
    print sql
    cursor.execute(sql, "2")
    result = cursor.fetchall()
    db.connection.commit()
    # export_excel("tt", result)
    export_txt("tangtang",result)

