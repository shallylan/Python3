# -*- coding:utf-8 -*-

import scrapy

class shiyanlouscoursesspider(scrapy.Spider):
	name = 'shiyanlou-courses'
	def start_request(self):
		url_templ = ['https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page=%d' %(n) for n in range(1,23)];
		urls= (url_teml.format(i) for i in range(1,23))

		for url in urls:
				yield scrapy.Request(url=url, callback = self.parse)

	def parse(self,response):
		for course in response.css(div.course-body):
			yield {
					'name': course.css('div.course-name::text').extract_first(),
					'description': course.css('div.course-desc::test').extract_first(),
					'student': course.xpath('//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d)[^\d]*')
					#'course_name': course.xpath('//h1/text()').extract()
					#'course_info': course.xpath('//h2/text()').extract_first()
			}