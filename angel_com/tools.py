def get_title(response):
    try:
        title = response.xpath("//h1[contains(@class, 'js-startup_name')]/text()").extract()[0]
        title = title.strip()
    except IndexError:
        title = "null"

    return title


def get_description(response):
    try:
        description = response.xpath("//div[contains(@class, 'product_desc')]/div/div[@class='content']/text()").extract()[0]
        description = description.strip()
    except IndexError:
        description = "null"

    return description
