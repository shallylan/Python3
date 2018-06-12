import scrapy

class challenge(scrapy.Spider):
	name = 'my challenge'
	start_urls = ['https://github.com/shiyanlou?page=%d&tab=repositories' % (n) for n in range(1,5)]
	print(start_urls)

	def parse(self,response):
		for a in response.xpath('//div[@id="user-repositories-list"]'):
			yield {
				'name':a.xpath('//div[@class="d-inline-block mb-1"]/h3/a/text()').re('[\n\s]*(.+)'),
				'updatetime':a.xpath('//div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract()
			}

#from scrapy import cmdline
#cmdline.execute("scrapy runspider Challenge15.py".split())