# -*- coding: utf-8 -*-
import scrapy
import re
from datacollect.items import DatacollectItem
from bs4 import BeautifulSoup


class datacollect(scrapy.Spider):  # 需要继承scrapy.Spider类

    name = "datacollect2"  # 定义蜘蛛名

    def start_requests(self):  # 由此方法通过下面链接爬取页面

        # 定义爬取的链接
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                   'Cache-Control': 'max-age=0',
                   'Cookie': '',
                   'Host': 'ask.qiuyi.cn',
                   'Proxy-Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

        urls = [
            'http://ask.qiuyi.cn/departments/207_1/index.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url,headers=headers, callback=self.parse1)  # 爬取到的页面如何处理？提交给parse方法处理

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

        # soup = BeautifulSoup(html)
        # next_page_url = soup.select('div[class="page"] a[class="next"]')[1].attrs["href"]

        # next_page_url = response.xpath ("//div[[contains(concat(' ', normalize-space(@class), ' '),' page ')]/a[2]/@href").extract()
        next_page_url = response.xpath(
            "//div[contains(concat(' ', normalize-space(@class), ' '),' page ')]/a[contains(concat(' ', normalize-space(@class), ' '),' next ')][2]/@href").extract()

        url_tag_list = response.xpath("//ul[contains(concat(' ', normalize-space(@class), ' '),' active ')]/li/span[1]/a[2]")



        for tagA in url_tag_list:
            try:
                item = DatacollectItem()

                item['title'] = tagA.xpath("text()").extract()[0]
                item['url'] = tagA.attrib["href"]

                # 这里是用的yield 而不是return
                print item['url']
                yield scrapy.Request(item['url'], callback=self.detail_parse,meta={"item": item})  # 爬取到的页面如何处理？提交给parse方法处理
            except Exception, e:
                print e
        else:
            if (len(next_page_url) > 0):
                yield scrapy.Request(next_page_url[0], callback=self.parse1)  # 爬取到的页面如何处理？提交给parse方法处理
            else:
                print "已经到最后一页"


    def detail_parse(self, response):

        html = response.text
        # item = response.meta['item']
        content = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '),' answer ')]/div/div[contains(concat(' ', normalize-space(@class), ' '),' wd_cont_s ')]")
        reg = r'<p><em>.*?</em>(.*?)</p>'
        answer = re.findall(reg, html, re.S)

        item = response.meta["item"]

        item["answer"] = answer[0]
        item["source"] = "求医网"

        yield item

    # page = response.url.split("/")[-2]  # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
    # filename = 'mingyan-%s.html' % page  # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
    # with open(filename, 'wb') as f:  # python文件操作，不多说了；
    #     f.write(response.body)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
    # self.log('保存文件: %s' % filename)  # 打个日志
