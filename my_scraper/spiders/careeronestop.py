# -*- coding: utf-8 -*-
import scrapy
from urlparse import urljoin
from scrapy import Request

import my_scraper.tools.careeronestop_tools as tools

url_pattern = 'http://www.careeronestop.org/businesscenter/\
findjobcenters/american-job-center-finder.aspx?location={}'


class CareeronestopSpider(scrapy.Spider):
    name = "careeronestop"
    allowed_domains = ["careeronestop.org"]
    '''
    start_urls = (
        'http://www.careeronestop.org/businesscenter/findjobcenters/american-job-center-finder.aspx?location=AL',
        'http://www.careeronestop.org/businesscenter/findjobcenters/american-job-center-finder.aspx?location=AK',
    )
    '''
    start_urls = [url_pattern.format(state) for state in tools.states]

    def parse(self, response):
        # block_xp = "//tr[@class='even' or @class='odd']//a/data/text()"
        block_xp = "//tr[@class='even' or @class='odd']"

        for block in response.xpath(block_xp):
            center_name = block.xpath(".//a/data/text()").extract_first()

            email_block = block.xpath(".//div[@id='centerNameChk']/input")

            emails = tools.get_emails(email_block)

            phone_xp = ".//div[@class='tel']/span[2]/data/text()"
            phone = block.xpath(phone_xp).extract_first()

            yield dict(center_name=center_name, emails=emails, phone=phone)

        # next page
        next = response.xpath("//a[@class='next-page']/@href").extract_first()
        if next:
            url = urljoin("http://careeronestop.org", next)
            yield Request(url, callback=self.parse)
