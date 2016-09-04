# -*- coding: utf-8 -*-
import scrapy
import my_scraper.tools.JujuTools as tools
from urlparse import urljoin


class JujuSpider(scrapy.Spider):
    name = "juju"
    allowed_domains = ["juju.com"]
    start_urls = (
        'http://www.juju.com/jobs?k=ESL+teacher/',
    )

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'my_scraper.middlewares.JuJuMiddleware': 543,
        }
    }

    def parse(self, response):
        search_results = response.xpath("//ul[@class='job_results']")
        search_item_xp = ".//a[contains(@class, 'result')]"

        for job_url in search_results.xpath(search_item_xp):
            job_href = job_url.xpath("@href").extract()[0]
            job_title = job_url.xpath("@title").extract()[0]
            rq = scrapy.Request(job_href, callback=self.parse_job)
            rq.meta['job_title'] = job_title
            yield rq

        # Next page.
        next_xp = "//a[@title='Next Page']/@href"
        next = response.xpath(next_xp).extract()
        if next:
            next_url = urljoin(self.start_urls[0], next[0])
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_job(self, response):

        if response.url in tools.broken_links:
            yield None

        title = response.meta['job_title']

        desc = tools.get_juju_description(response)

        yield dict(title=title,
                   description=desc,
                   url=response.url)
