# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# importing the required libraries
import scrapy

# Creating a class of items to store the elements extracted using the CSS/Xpath selector elements
class GlassdoorItem(scrapy.Item):
    # define the fields for your item here like:
    rating = scrapy.Field()
    employee_type = scrapy.Field()
    review = scrapy.Field()
    date_position = scrapy.Field()
    pros = scrapy.Field()
    cons = scrapy.Field()
    pass
