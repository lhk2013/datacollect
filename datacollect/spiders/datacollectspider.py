# -*- coding: utf-8 -*-
import scrapy
import re
from datacollect.items import DatacollectItem
from bs4 import BeautifulSoup


class datacollect(scrapy.Spider):  # 需要继承scrapy.Spider类


    name = "datacollect2"  # 定义蜘蛛名

    allowed_domains = ['www.jianke.com']


    # start_urls = ['https://www.jianke.com/jibing/keshi/40']

    def start_requests(self):  # 由此方法通过下面链接爬取页面

        # 定义爬取的链接
        urls = [
            'https://www.jianke.com/jibing/keshi/40'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse1)  # 爬取到的页面如何处理？提交给parse方法处理


    def parse1(self, response):
        '''
        start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        就是这么个流程，似不似很简单呀？
        '''

        html = response.text
        # print html
        # reg = r'<div class="ks_list_xl">(.*?)</div>'
        # infos = re.findall(reg, html, re.S)

        soup = BeautifulSoup(html)
        infos = soup.select('div[class="ks_list"] div[class="ks_list_xl"] ul li a ')


        catUrlList = []
        for cat in infos:
            try:
                item = DatacollectItem()

                item['name'] = cat.text.encode("utf8")
                item['href'] = cat.attrs["href"]
                item['url'] = "https://www.jianke.com" + item['href']
                next_url = "https://www.jianke.com/jibing/keshi/770"
                # 这里是用的yield 而不是return
                # yield item
                yield scrapy.Request(next_url,callback=self.detail_parse)  # 爬取到的页面如何处理？提交给parse方法处理
            except Exception,e:
                print e
    def detail_parse(self, response):

        html = response.text
        # item = response.meta['item']

        print html
        item = DatacollectItem()

        yield item

    # page = response.url.split("/")[-2]  # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        # filename = 'mingyan-%s.html' % page  # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        # with open(filename, 'wb') as f:  # python文件操作，不多说了；
        #     f.write(response.body)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        # self.log('保存文件: %s' % filename)  # 打个日志