# -*- coding:utf-8 -*-

import scrapy



class scrapy_practice(scrapy.Spider):
    name = 'shiyanlou-courses'
    start_urls = ['https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page=%d' % (n) for n in range(1, 23)]
    print(start_urls)

    # def start_request(self):
    #     for url in start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        for course in response.css('div.course-body'):
            yield {
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'student': course.xpath('//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d)[^\d]*')
            }


#from scrapy import cmdline
#cmdline.execute("scrapy runspider scrapy_practice_zp.py".split())