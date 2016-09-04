import bs4
from urlparse import urlparse
import scrapy.exceptions
import re


class Parser:
    def __init__(self):
        self.parsers = {
            'www.juju.com': self.juju_com,

            'www.ihiresecondaryteachers.com': self.ihiresecondaryteachers_com,
            'www.ihireelementaryteachers.com': self.ihiresecondaryteachers_com,
            'www.ihireschooladministrators.com': self.ihiresecondaryteachers_com,

            'www.themuse.com': self.themuse_com,
            'www.startwire.com': self.startwire_com,
            'internationaleducationgroup.applytojob.com': self.internationaleducationgroup_applytojob_com,
            'recruit.zohopublic.com': self.recruit_zohopublic_com,
            'www.glassdoor.com': self.glassdoor_com,
            'anyonehiring.com': self.anyonehiring_com,
            'careers.novastarprep.com': self.careers_novastarprep_com,
            'jobs.houstonisd.org': self.jobs_houstonisd_org,
            'xcelhr.catsone.com': self.xcelhr_catsone_com,
            'apply.embassysummer.com': self.apply_embassysummer_com,
            'takelessons.com': self.takelessons_com,
            'www.hirebridge.com': self.hirebridge_com,
            'www.englishfirst.com': self.englishfirst_com,
            'www.careerbuilder.com': self.careerbuilder_com,
            'jobs.mpls.k12.mn.us': self.jobs_mpls_k12_mn_us,
            'minnesotajobs.com': self.minnesotajobs_com,
            'vipkid.us': self.vipkid_us,
            'main.hercjobs.org': self.main_hercjobs_org,
            'jobs.washingtonpost.com': self.jobs_washingtonpost_com,
            'buffaloschools.applicantstack.com': self.buffaloschools_applicantstack_com,
            'www.prodivnet.com': self.www_prodivnet_com,
            'sais.associationcareernetwork.com': self.sais_associationcareernetwork_com,
            'legalforce.applytojob.com': self.legalforce_applytojob_com,
            'educators-on-call.workable.com': self.educators_on_call_workable_com,
            'switchrecruit.catsone.com': self.switchrecruit_catsone_com,
            'www.JobsInME.com': self.www_JobsInME_com,
            'www.jobsinme.com': self.www_JobsInME_com,
            'studygroup.applytojob.com': self.studygroup_applytojob_com,

            'www.disabledperson.com': self.www_disabledperson_com,
            'www.vscyberhosting3.com': self.www_vscyberhosting3_com,
            'www.ivyexec.com': self.www_ivyexec_com,
            'careers.insidehighered.com': self.careers_insidehighered_com,
        }

    def get_parser(self, netloc):
        return self.parsers[netloc]

    def juju_com(self, soup):
        try:
            desc = soup.find("dd", attrs={'class': 'description'})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def themuse_com(self, soup):
        try:
            desc = soup.find("div", attrs={'class': 'job-post-description'})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def ihiresecondaryteachers_com(self, soup):
        try:
            desc = soup.find("div", attrs={'class': 'job-description'})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def startwire_com(self, soup):
        try:
            desc = soup.find("div", attrs={'class': 'ua-job-description'})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def internationaleducationgroup_applytojob_com(self, soup):
        try:
            desc = soup.find("div", attrs={"id": "resumator-job-description"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def buffaloschools_applicantstack_com(self, soup):
        try:
            desc = soup.find("div", id="ascontainer").div.next_siblings
            desc = list(desc)[1].get_text(" ", strip=True)
        except IndexError:
            desc = "null"

        return desc

    def recruit_zohopublic_com(self, soup):
        return "js site"

    def glassdoor_com(self, soup):
        return "js site"

    def anyonehiring_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "job-leftcontent"}).next_siblings
            desc = list(desc)[1].get_text(" ", strip=True)
        except IndexError:
            desc = "null"

        return desc

    def careers_novastarprep_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "detailsJobDescription"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def jobs_houstonisd_org(self, soup):
        try:
            desc = soup.find("div", attrs={"class", "jobDisplay"})
            # Remove js
            [i.extract() for i in desc.find_all("script")]
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def xcelhr_catsone_com(self, soup):
        try:
            desc = soup.find("tr", id='trpositionsummary')
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def apply_embassysummer_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "description"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def takelessons_com(self, soup):
        try:
            desc = soup.find("article", id="Listing")
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def hirebridge_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "main"}).article
            [i.extract() for i in desc.find_all("script")]
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def englishfirst_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class", "describe"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def careerbuilder_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class", "description"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def jobs_mpls_k12_mn_us(self, soup):
        try:
            desc = soup.find("div", attrs={"class", "jobDisplay"})
            [i.extract() for i in desc.find_all("script")]
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def minnesotajobs_com(self, soup):
        try:
            desc = soup.find_all("div", attrs={"class": "view_long"})[1]
            desc = desc.get_text(" ", strip=True)
        except IndexError:
            desc = "null"

        return desc

    def vipkid_us(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "job-posting"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def main_hercjobs_org(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "bti-jd-description"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def jobs_washingtonpost_com(self, soup):
        try:
            desc = soup.find("div", attrs={"itemprop": "description"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def www_prodivnet_com(self, soup):
        try:
            desc = soup.find("div", id="description")
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def sais_associationcareernetwork_com(self, soup):
        try:
            desc = soup.find("span", id="lblJobDesc")
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def legalforce_applytojob_com(self, soup):
        try:
            desc = soup.find("div", id="resumator-job-description")
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def educators_on_call_workable_com(self, soup):
        try:
            desc = soup.find("section", attrs={"class": "section section--text"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def switchrecruit_catsone_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "detailsJobDescription"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def www_JobsInME_com(self, soup):
        try:
            desc = soup.find("p", id="docs-internal-guid-c9adc6d3-8e76-4327-a73d-44b8e48e759a")
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def studygroup_applytojob_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "description"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def www_disabledperson_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "job"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def www_vscyberhosting3_com(self, soup):
        try:
            desc = soup.find("table", id="CRCareers1_tblJobDescrDetail")
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc

    def www_ivyexec_com(self, soup):
        try:
            desc = soup.find("div", attrs={"class": "main-content"})
            desc = desc.find_all("div", attrs={"class": "row-fluid"})[3]
            desc = desc.get_text(" ", strip=True)
        except IndexError:
            desc = "null"

        return desc

    def careers_insidehighered_com(self, soup):
        try:
            desc = soup.find("div", attrs={"itemprop": "description"})
            desc = desc.get_text(" ", strip=True)
        except AttributeError:
            desc = "null"

        return desc


def clean_desc(desc):

    # Delete phones.
    strip_phone = re.compile(r"\(?\d+\)?-?\d+-?\d+-?\d*")
    desc = strip_phone.sub("", desc)

    # Delete mails.
    strip_phone = re.compile(r"\w+@\w+\.\w+")
    desc = strip_phone.sub("", desc)

    # Strip www.
    strip_www = re.compile(r"http://\w*.?\w+\.(com|org|net)")
    desc = strip_www.sub("", desc)

    return desc


def get_juju_description(response):
    body = response.xpath("//body").extract()[0]
    soup = bs4.BeautifulSoup(body, "lxml")
    netloc = urlparse(response.url).netloc
    try:
        parser = Parser().get_parser(netloc)
    except KeyError:
        raise scrapy.exceptions.CloseSpider("No parser for: [{}],\
 netloc: [{}]".format(response.url, netloc))

    desc = parser(soup)

    if desc != "null":
        desc = clean_desc(desc)

    return desc

broken_links = [
    'https://www.workable.com/',

    'http://www.prodivnet.com/job-summaries?\
job=5799e554e796554880000348&organization=Chicago+Public+Schools',
    'http://www.prodivnet.com/job-summaries?\
job=57a07b6ee79655a32100156c&organization=Chicago+Public+Schools',
    'http://www.prodivnet.com/job-summaries?\
job=57934e59e79655741200133b&organization=Chicago+Public+Schools',
    'http://www.prodivnet.com/job-summaries?\
job=5799e624e79655488000038c&organization=Chicago+Public+Schools',
    'http://www.prodivnet.com/job-summaries?\
job=57a0760fe79655b30a0001ef&organization%20=Seattle+Public+Schools',
    'http://www.prodivnet.com/job-summaries?\
job=57a0760fe79655b30a0001ef&organization=Seattle+Public+Schools',

    'http://jobsearch.educationamerica.net/index.phtml?a=v&',
    'http://findjobinfo.com',

    'https://simplyjobs.com/applicants/register/sign-up?\
feed=DirectEmployers&job_id=iCIMS14507-5975',
    'https://simplyjobs.com/applicants/register/sign-up?\
feed=DirectEmployers&job_id=iCIMS14507-5877'
]
