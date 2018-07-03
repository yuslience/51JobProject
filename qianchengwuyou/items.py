# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengwuyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job = scrapy.Field()
    job_link = scrapy.Field()
    company_name = scrapy.Field()
    location = scrapy.Field()
    publish_date = scrapy.Field()
    salary = scrapy.Field()
    experience_rqs = scrapy.Field()
    job_desc = scrapy.Field()
    job_desc_list = scrapy.Field()
