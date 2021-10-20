# Importing the class from items.py and other libraries required for webscraping
import scrapy
from ..items import GlassdoorItem

# This spider class helps in extracting the required information using xpath/css selector
class GlassdoorSpiderSpider(scrapy.Spider):
    name = 'glassdoor_spider'
    page_number = 1
    # The website home url that is to be scraped should be posted below. 
    allowed_domains = ['glassdoor.com']
    # Provide the start url for spider to reference the initial website below. 
    start_urls = ['https://www.glassdoor.com/Reviews/Walmart-Reviews-E715.htm?filter.iso3Language=eng']
    
    def parse(self, response):
        items = GlassdoorItem()
        
        rating = response.css("#ReviewsFeed .mr-xsm").css("::text").extract()
        employee_type = response.css(".eg4psks0").css("::text").extract()
        review = response.css(".reviewLink").css("::text").extract()
        date_position = response.css(".middle.common__EiReviewDetailsStyle__newGrey").css("::text").extract()
        pros = response.css(".v2__EIReviewDetailsV2__fullWidth:nth-child(1) span").css("::text").extract()
        cons = response.css(".v2__EIReviewDetailsV2__fullWidth+ .v2__EIReviewDetailsV2__fullWidth span").css("::text").extract()
        
        items['rating'] = rating
        items['employee_type'] = employee_type
        items['review'] = review
        items['date_position'] = date_position
        items['pros'] = pros
        items['cons'] = cons

        yield items
# Pagination done through the next page element, helps cycle the scraping process across each page till it reaches the limit set by user below. 
        next_page = "https://www.glassdoor.com/Reviews/Walmart-Reviews-E715_P"+ str(GlassdoorSpiderSpider.page_number) +".htm?filter.iso3Language=eng"
        if GlassdoorSpiderSpider.page_number <= 2:
            GlassdoorSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)