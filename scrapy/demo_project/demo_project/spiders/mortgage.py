import scrapy 
from demo_project.items import FixedMortgageItem, CustomLoader, VariableMortgageItem
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
        for fix_rate in response.xpath("//div[@class='table-responsive margin-bottom']"):
            l = CustomLoader(item = FixedMortgageItem(), selector = fix_rate)
            l.add_xpath('fix_insured_mortgage_rate',"//div[@class='table-responsive margin-bottom']/table/tbody/tr/td")
            l.add_xpath('fix_conventional_mortgage_rate',"//div[@class='table-responsive margin-bottom']/table/tbody/tr/td")
            l.add_xpath('fix_insured_mortgage_rate_time',"//div[@class='table-responsive margin-bottom']/table/tbody/tr/td/@aria-label")
            l.add_xpath('fix_conventional_mortgage_rate_time',"//div[@class='table-responsive margin-bottom']/table/tbody/tr/td/@aria-label")
            yield l.load_item()


        for variable_rate in response.xpath("//p[@class='o-text-small']"):
            r = CustomLoader(item = VariableMortgageItem(), selector = variable_rate)
            r.add_xpath('variable_insured_mortgage_rate', "//p[@class='o-text-small']")
            r.add_xpath('variable_conventional_mortgage_rate', "//p[@class='o-text-small']")
            r.add_xpath('open_mortgage_rate', "//p[@class='o-text-small']")
            yield r.load_item()
   