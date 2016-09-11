# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    start_urls = (
        'http://www.indeed.com/q-esl-teacher-jobs.html/',
    )

    def parse(self, response):
        search_results = response.xpath("")
