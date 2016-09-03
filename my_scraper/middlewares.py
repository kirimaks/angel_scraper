from scrapy.exceptions import IgnoreRequest
from my_scraper.tools.JujuTools import broken_links


class JuJuMiddleware(object):
    def process_response(self, request, response, spider):
        if response.url in broken_links:
            print("\n\n\n\n **** ")
            print("URL: ", response.url)
            print("Ignore??\n\n\n")
            raise IgnoreRequest

        return response
