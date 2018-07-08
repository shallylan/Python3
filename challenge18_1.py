#-*- utf: 8 -*-

import json

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

results = []

def parse(response):
	for comment in response.css('div.comment-list'):
		name = comment.xpath('//a[@class="username"]/text()').re_first('[\S]*(.+)[\S]')
		comcontent = comment.xpath('//div[@class="comment-item-content markdown-box"]/@p/text()').extract_first()
		result[name] = comcontent
		TODO
		results.append(result)

def has_next_page(response):
	pageination = response.xpath('//div[@class="pageination-container"]/ul/@class').extract_first()
	if pageination == "pageination":
		a = True
	else:
		a = False
	
	return a

def goto_next_page(driver):
	driver.find_element_by_xpath('.//li[@class="next-page"]/a/@href').click()
	TODO

def wait_page_return(driver, page):
	WebDriverWait(driver, 10).until(
		EC.text_to_be_present_in_element(
			(By.XPATH, '//ul[@class="pageination"]/li[@class="active"]'),
			str(page)
		)
	)
#主函数
def spider():
	driver = webdriver.PhantomJS()
	url = 'https://www.shiyanlou.com/courses/427'
	driver.get(url)
	page = 1
	while True:
		wait_page_return(driver, page)
		html = driver.page_source
		response = HtmlResponse(url=url, body=html.encode('utf8'))
		parse(response)
		if not has_next_page(response):
			break
		page +=1
		goto_next_page(river)
	with open('home/shiyanlou/comments.json', 'w') as f:
		f.write(json.dumps(results))

if __name__ == '__main__':
	spider()
