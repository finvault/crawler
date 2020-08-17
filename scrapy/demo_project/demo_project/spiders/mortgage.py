import scrapy 
from demo_project.items import FixedMortgageItem, CustomLoader
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from scrapy import Request

class MortgageSpider(scrapy.Spider):
    name = 'mortgage'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = [ 'https://www.firstnational.ca/residential/mortgage-rates'
        
    ]
    handle_httpstatus_list = [404]


    def parse(self, response):
        for fix_rate in response.xpath("//table"):
            l = CustomLoader(item = FixedMortgageItem(), selector = fix_rate)
            l.add_xpath('fix_insured_mortgage_rate',"//table/tbody/tr/td")
            l.add_xpath('fix_insured_mortgage_rate',"//table/tbody/tr/th")
            yield l.load_item()


     
   