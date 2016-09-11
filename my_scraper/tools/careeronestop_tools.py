import re

email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")


def get_emails(resp):
    emails_buff = list()

    for attr in ["@data-generalemail", "@data-vetemail", "@data-busemail"]:
        emails = resp.xpath(attr).extract_first()
        emails = emails.split(";")
        for email in emails:
            if email_pattern.match(email):
                emails_buff.append(email.strip())

    emails_buff = filter(lambda l: len(l) > 1, emails_buff)
    return emails_buff


states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID',
    'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
    'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
    'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
    'WI', 'WY', 'GU', 'PR'
]
