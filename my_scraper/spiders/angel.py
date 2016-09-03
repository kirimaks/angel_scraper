# -*- coding: utf-8 -*-
import scrapy
import json
from bs4 import BeautifulSoup
from scrapy import FormRequest, Request
from urllib import urlencode
import my_scraper.tools.AngelTools as tools


class AngelSpider(scrapy.Spider):
    name = "angel"
    allowed_domains = ["angel.co"]
    start_urls = (
        'https://angel.co/company_filters/search_data',
    )

    def __init__(self, *pargs, **kwargs):
        scrapy.Spider.__init__(self, *pargs, **kwargs)
        self.pages = 20

    def parse(self, response):

        formdata = {
            "filter_data[markets][]": "Education",
            "filter_data[company_types][]": "Startup",
            "sort": "signal",
            # "page": "2"
        }

        headers = {
            "Referer": "https://angel.co/companies?markets[]=Education&company_types[]=Startup",
            "X-Requested-With": "XMLHttpRequest"
        }

        for i in range(1, self.pages + 1):
            formdata['page'] = str(i)
            yield FormRequest(url=response.url, formdata=formdata,
                              callback=self.form_response,
                              headers=headers)

    def form_response(self, response):
        company_ids = json.loads(response.text)
        self.logger.debug("### form response ###: {}".format(company_ids))
        company_ids["ids[]"] = company_ids["ids"]
        company_ids.pop("ids")
        # print(company_ids)
        qs = urlencode(company_ids, doseq=True)
        # print(qs)
        url = "https://angel.co/companies/startups?{}".format(qs)
        yield Request(url, callback=self.company_list)

    def company_list(self, response):
        company_data = json.loads(response.text)
        company_soup = BeautifulSoup(company_data['html'], "lxml")

        company_list = company_soup.findAll("a",
                                            attrs={"class": "startup-link"})
        for company in company_list:
            # print(company['href'])
            yield Request(company['href'], callback=self.parse_company)

    def parse_company(self, response):
        title = tools.get_title(response)
        description = tools.get_description(response)

        yield dict(title=title, description=description,
                   url=response.url)
