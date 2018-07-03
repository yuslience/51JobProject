# -*- coding: utf-8 -*-
import scrapy
from ..items import QianchengwuyouItem

class JoblistSpider(scrapy.Spider):
    name = 'joblist'
    allowed_domains = ['search.51job.com']
    start_urls = ['https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        div_list = response.xpath('//div[@id="resultList"]/div')[3:53]
        for div in div_list:
            item = QianchengwuyouItem()
            job = div.xpath('./p/span/a/@title').extract_first()
            job_link = div.xpath('.//p/span/a/@href').extract_first()
            company_name = div.xpath('./span/a/@title').extract_first()
            location = div.xpath('./span[2]/text()').extract_first()
            salary = div.xpath('./span[3]/text()').extract_first()
            publish_date = div.xpath('./span[4]/text()').extract_first()
            item['job'] = job
            item['job_link'] = job_link
            item['company_name'] = company_name
            item['location'] = location
            item['salary'] = salary
            item['publish_date'] = publish_date
            # yield item
            yield scrapy.Request(job_link,callback=self.parse_detail,meta={'item':item},dont_filter=True)

        for i in range(2,103):
            url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,%d.html' % i
            yield scrapy.Request(url,callback=self.parse)


    def parse_detail(self,response):
        item = response.meta['item']

        experience_rqs = response.xpath('//div[@class="t1"]/span/text()')
        experience_rqs=str([x.extract() for x in experience_rqs])

        job_desc= response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')
        job_desc=str([x.extract() for x in job_desc])

        item['experience_rqs'] = experience_rqs
        item['job_desc'] = job_desc
        yield item





























