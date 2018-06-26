# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import RepositoryItem


class RepositorySpider(scrapy.Spider):
    name = 'repository'
    #allowed_domains = ['github.com']
    start_urls = ['http://github.com/shiyanlou?page=%d&tab=repositories' %(n) for n in range(1,5)]

    def parse(self, response):
        #for i in response.xpath('.//li[@class="col-12 d-block width-full py-4 border-bottom public source"]'):
        for i in response.css('li.col-12'):
            item = RepositoryItem()

            item['name'] = i.xpath('.//a/text()').re_first('[\S+](.+)[\S]*')

            item['update_time'] = i.xpath('.//relative-time/@datetime').extract_first()

            repository_url = response.urljoin(i.xpath('.//a/@href').extract_first())

            request = scrapy.Request(repository_url, callback=self.parse_details)

            request.meta['item'] = item

            yield request


    def parse_details(self, response):
        item = response.meta['item']
        item['commits'] = response.css('span.num::text').extract()[0].strip()
        item['branches'] = int(response.css('span.num::text').extract()[1].strip())
        item['releases'] = int(response.css('span.num::text').extract()[2].strip())
        '''
        j = response.xpath('//h1[@class="public"]/strong/a/text()')


        item['commits'] = response.xpath('.//li[@class="commits"]/a/span/text()').re_first('[\S](\d+)[\S]*')

        item['branches'] = response.xpath('.//a[@href="shiyanlou/j/branches"]/span/text()').re_first('[\S+](\d+)[\S]*')

        item['releases'] = response.xpath('.//a[@href="shiyanlou/j/releases"]/span/text()').re_first('[\S+](\d+)[\S]*')
        '''
        yield item

