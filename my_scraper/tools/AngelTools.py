def get_title(response):
    try:
        title = response.xpath("//h1[contains(@class, 'js-startup_name')]\
/text()").extract()[0]
        title = title.strip()
    except IndexError:
        title = "null"

    return title


def get_description(response):
    desc = list()

    # Get visible description.
    desc_xp = "//div[contains(@class, 'product_desc')]\
/div/div[@class='content']/text()"
    for d in response.xpath(desc_xp).extract():
        desc.append(d.strip())

    # Get hidden description.
    hidden_desc_xp = "//div[contains(@class, 'product_desc')]\
/div/div[@class='content']/span[@class='hidden']/text()"

    for d in response.xpath(hidden_desc_xp).extract():
        desc.append(d.strip())

    if not desc:
        desc = "null"
    else:
        desc = str.join(" ", desc)

    return desc
