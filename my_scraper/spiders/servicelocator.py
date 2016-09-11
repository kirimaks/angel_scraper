# -*- coding: utf-8 -*-
import scrapy
from urlparse import urljoin
from scrapy import Request

import re

search_emails = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")


class ServicelocatorSpider(scrapy.Spider):
    name = "servicelocator"
    allowed_domains = ["www.servicelocator.org"]
    start_urls = (
        'http://www.servicelocator.org/search/CategorySearch_Result.asp?\
zip=&city=&state=&proximity=25&officeType_1=103&prgcat=4',
    )

    def parse(self, response):
        link_xp = "//span[@class='body10pt appreenticeName']"
        for line in response.xpath(link_xp):
            url = line.xpath(".//a/@href").extract()[0]
            url = urljoin("http://www.servicelocator.org/search/", url)
            yield Request(url, callback=self.parse_page)

        # next page
        next_xp = "//img[@alt='Go Next']/parent::a/@href"

        next = response.xpath(next_xp).extract_first()
        if next:
            url = urljoin("http://www.servicelocator.org", next)
            print("\n\nNext url", url)
            yield Request(url, callback=self.parse)

    def parse_page(self, response):
        email_xp = "//strong[contains(text(), 'Contact Email Address')]\
/parent::div/parent::td/following-sibling::td//a/text()"
        email = response.xpath(email_xp).extract_first()

        if email:
            email = email.strip()

            name_xp = "//strong[contains(text(), 'Contact Name')]\
/parent::div/parent::td/following-sibling::td/div/text()"
            name = response.xpath(name_xp).extract_first()
            name = name.strip() if name else ""

            yield dict(url=response.url, email=email, name=name)
